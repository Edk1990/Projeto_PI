from flask import Flask, request, jsonify, render_template, send_from_directory, send_file, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
import shutil
import pandas as pd
from io import BytesIO

app = Flask(__name__, static_folder='.', static_url_path='')
# Configuração do banco de dados: usa o DATABASE_URL do Heroku (Postgres) se disponível, senão, usa o SQLite local.
database_url = os.environ.get('DATABASE_URL')
if database_url:
    # O Heroku usa 'postgres://', mas SQLAlchemy espera 'postgresql://'
    database_url = database_url.replace('postgres://', 'postgresql://')
app.config['SQLALCHEMY_DATABASE_URI'] = database_url or 'sqlite:///pesquisa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Credenciais do administrador
ADMIN_CREDENTIALS = {
    'email': 'admin',
    'password': 'admin'
}

# Modelo para armazenar as respostas da pesquisa
class Resposta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120))
    data_visita = db.Column(db.String(10))
    placa = db.Column(db.String(8))
    consultor = db.Column(db.String(100))
    motivo_visita = db.Column(db.String(100))
    problema_resolvido = db.Column(db.String(3))
    problema_nao_resolvido = db.Column(db.String(500))
    sugestoes = db.Column(db.String(500))
    probability = db.Column(db.Integer)
    data_resposta = db.Column(db.DateTime, default=datetime.utcnow)

# Função para criar o banco de dados
def recreate_database():
    try:
        # Remover o banco de dados existente se existir
        if os.path.exists('pesquisa.db'):
            os.remove('pesquisa.db')
        
        # Criar novo banco de dados
        db.create_all()
        
        # Criar uma resposta de teste para garantir que a tabela foi criada corretamente
        teste = Resposta(
            email='teste@teste.com',
            data_visita='2025-05-25',
            placa='XXX-0000',
            consultor='Teste',
            motivo_visita='Teste',
            problema_resolvido='Sim',
            problema_nao_resolvido='',
            sugestoes='Teste',
            probability=100
        )
        db.session.add(teste)
        db.session.commit()
        
        return True
    except Exception as e:
        print(f"Erro ao criar banco de dados: {str(e)}")
        return False

# A linha abaixo foi comentada para não apagar o banco de dados em produção a cada reinicialização.
# Para criar o banco de dados pela primeira vez no Heroku, use: heroku run python -c "from app import db; db.create_all()"
# with app.app_context():
#     db.create_all() # Apenas cria as tabelas se não existirem

@app.route('/submit', methods=['POST'])
def submit_survey():
    try:
        data = request.form
        
        # Criar nova resposta
        resposta = Resposta(
            email=data.get('email'),
            data_visita=data.get('date'),
            placa=data.get('plate'),
            consultor=data.get('consultant'),
            motivo_visita=data.get('reason'),
            problema_resolvido=data.get('resolved'),
            problema_nao_resolvido=data.get('unresolved_reason', ''),
            sugestoes=data.get('suggestions', ''),
            probability=int(data.get('probability', 0))
        )
        
        # Salvar no banco
        db.session.add(resposta)
        db.session.commit()
        
        return jsonify({'success': True}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/admin/login', methods=['POST'])
def admin_login():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        
        # Verifica se o email começa com 'admin' e a senha está correta
        if email and email.lower().startswith('admin') and password == ADMIN_CREDENTIALS['password']:
            return jsonify({'success': True}), 200
        else:
            return jsonify({'success': False, 'message': 'Credenciais inválidas'}), 401
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/admin/respostas', methods=['GET'])
def get_respostas():
    try:
        respostas = Resposta.query.order_by(Resposta.data_resposta.desc()).all()
        return jsonify([{
            'id': r.id,
            'email': r.email,
            'data_visita': r.data_visita,
            'placa': r.placa,
            'consultor': r.consultor,
            'motivo_visita': r.motivo_visita,
            'problema_resolvido': r.problema_resolvido,
            'problema_nao_resolvido': r.problema_nao_resolvido,
            'sugestoes': r.sugestoes,
            'probability': r.probability,
            'data_resposta': r.data_resposta.strftime('%Y-%m-%d %H:%M:%S')
        } for r in respostas])
    except Exception as e:
        return jsonify({'error': str(e)}), 500



@app.route('/')
def index():
    return redirect(url_for('serve_static', path='tela__login.html'))


@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)



if __name__ == '__main__':
    app.run(debug=True, port=5000)
