from flask import Flask, request, jsonify, render_template, send_from_directory, send_file
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
import urllib.parse
import requests

app = Flask(__name__, static_folder='.', static_url_path='')

# Tenta pegar o banco do Railway; se não achar, usa o SQLite local
uri = os.environ.get("DATABASE_URL", "sqlite:///pesquisa.db")

# Corrige o prefixo exigido pelo SQLAlchemy moderno
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def home():
    # Isso faz o link principal abrir a sua tela de login automaticamente
    return app.send_static_file('tela_login.html')

# Credenciais do administrador
ADMIN_CREDENTIALS = {
    'email': 'admin',
    'password': 'admin'
}

# Função para enviar mensagem no WhatsApp
def enviar_alerta_whatsapp(placa, consultor, problema_nao_resolvido, probabilidade):
    # O número deve estar sem o sinal de + para o CallMeBot funcionar bem
    telefone_gerente = "551900000000"  
    api_key = "6073595"         
    
    # Mensagem formatada com as variáveis
    mensagem = (
        f"🚨 *ALERTA DE CLIENTE INSATISFEITO* 🚨\n\n"
        f"🚗 *Placa:* {placa}\n"
        f"👨‍💼 *Consultor:* {consultor}\n"
        f"❌ *Problema:* {problema_nao_resolvido if problema_nao_resolvido else 'Não especificado'}\n"
        f"📉 *Chance de retorno:* {probabilidade}%\n\n"
        f"Por favor, verifique a situação imediatamente!"
    )
    
    # É obrigatório converter espaços e quebras de linha para o formato de link da internet
    mensagem_codificada = urllib.parse.quote(mensagem)
    
    try:
        # URL - Callmebot
        url = f"https://api.callmebot.com/whatsapp.php?phone={telefone_gerente}&text={mensagem_codificada}&apikey={api_key}"
        
        # Faz o disparo da mensagem
        resposta = requests.get(url)
        
        if resposta.status_code == 200:
            print("✅ Alerta de WhatsApp enviado com sucesso!")
        else:
            print(f"❌ Erro ao enviar WhatsApp: {resposta.text}")
            
    except Exception as e:
        print(f"❌ Erro na integração com WhatsApp: {e}")


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
        if os.path.exists('pesquisa.db'):
            os.remove('pesquisa.db')
        
        db.create_all()
        
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


# Criar o banco de dados inicial
with app.app_context():
    recreate_database()


@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Pega os dados que vieram do formulário HTML
        email = request.form.get('email', '')
        data_visita = request.form.get('date')
        placa = request.form.get('plate')
        consultor = request.form.get('consultant')
        motivo_visita = request.form.get('reason')
        problema_resolvido = request.form.get('resolved')
        problema_nao_resolvido = request.form.get('unresolved_reason', '')
        sugestoes = request.form.get('suggestions', '')
        
        # Garante que a probabilidade seja um número (inteiro)
        try:
            probability = int(request.form.get('probability', 0))
        except ValueError:
            probability = 0

        # CRIANDO O OBJETO
        nova_resposta = Resposta(
            email=email,
            data_visita=data_visita,
            placa=placa,
            consultor=consultor,
            motivo_visita=motivo_visita,
            problema_resolvido=problema_resolvido,
            problema_nao_resolvido=problema_nao_resolvido,
            sugestoes=sugestoes,
            probability=probability
        )

        # Salva no banco de dados
        db.session.add(nova_resposta)
        db.session.commit()

        # GATILHO DO WHATSAPP
        if problema_resolvido == 'Não' or probability <= 50:
            enviar_alerta_whatsapp(placa, consultor, problema_nao_resolvido, probability)
            
        return jsonify({'success': True}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/admin/login', methods=['POST'])
def admin_login():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        
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


@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)


if __name__ == '__main__':
    app.run(debug=True, port=5000)