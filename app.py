from flask import Flask, request, jsonify, render_template, send_from_directory, send_file
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

# Criar banco de dados automaticamente
with app.app_context():
    db.create_all()

# Rota principal - redireciona para página de login
@app.route('/')
def index():
    return send_from_directory('.', 'tela__login.html')

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

# ========================================
# API v1 - Endpoints versionados
# ========================================

@app.route('/api/v1/respostas', methods=['GET'])
def api_v1_get_all_respostas():
    """Listar todas as respostas com filtros opcionais"""
    try:
        query = Resposta.query
        
        # Filtros opcionais via query params
        consultor = request.args.get('consultor')
        data_inicio = request.args.get('data_inicio')
        data_fim = request.args.get('data_fim')
        
        if consultor:
            query = query.filter(Resposta.consultor.ilike(f'%{consultor}%'))
        if data_inicio:
            query = query.filter(Resposta.data_visita >= data_inicio)
        if data_fim:
            query = query.filter(Resposta.data_visita <= data_fim)
        
        respostas = query.order_by(Resposta.data_resposta.desc()).all()
        
        return jsonify({
            'success': True,
            'total': len(respostas),
            'data': [{
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
            } for r in respostas]
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/v1/respostas/<int:id>', methods=['GET'])
def api_v1_get_resposta_by_id(id):
    """Buscar resposta específica por ID"""
    try:
        resposta = Resposta.query.get(id)
        
        if not resposta:
            return jsonify({'success': False, 'error': 'Resposta não encontrada'}), 404
        
        return jsonify({
            'success': True,
            'data': {
                'id': resposta.id,
                'email': resposta.email,
                'data_visita': resposta.data_visita,
                'placa': resposta.placa,
                'consultor': resposta.consultor,
                'motivo_visita': resposta.motivo_visita,
                'problema_resolvido': resposta.problema_resolvido,
                'problema_nao_resolvido': resposta.problema_nao_resolvido,
                'sugestoes': resposta.sugestoes,
                'probability': resposta.probability,
                'data_resposta': resposta.data_resposta.strftime('%Y-%m-%d %H:%M:%S')
            }
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/v1/respostas/<int:id>', methods=['DELETE'])
def api_v1_delete_resposta(id):
    """Deletar resposta específica (apenas admin)"""
    try:
        resposta = Resposta.query.get(id)
        
        if not resposta:
            return jsonify({'success': False, 'error': 'Resposta não encontrada'}), 404
        
        db.session.delete(resposta)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': f'Resposta ID {id} deletada com sucesso'
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/v1/estatisticas', methods=['GET'])
def api_v1_get_estatisticas():
    """Obter estatísticas gerais das pesquisas"""
    try:
        total_respostas = Resposta.query.count()
        
        # NPS médio
        nps_medio = db.session.query(db.func.avg(Resposta.probability)).scalar() or 0
        
        # Problemas resolvidos vs não resolvidos
        problemas_sim = Resposta.query.filter_by(problema_resolvido='Sim').count()
        problemas_nao = Resposta.query.filter_by(problema_resolvido='Não').count()
        
        # Distribuição por consultor
        consultores = db.session.query(
            Resposta.consultor,
            db.func.count(Resposta.id).label('total'),
            db.func.avg(Resposta.probability).label('nps_medio')
        ).group_by(Resposta.consultor).all()
        
        # Distribuição de NPS por faixa
        detratores = Resposta.query.filter(Resposta.probability <= 6).count()  # 0-6
        neutros = Resposta.query.filter(Resposta.probability >= 7, Resposta.probability <= 8).count()  # 7-8
        promotores = Resposta.query.filter(Resposta.probability >= 9).count()  # 9-10
        
        return jsonify({
            'success': True,
            'data': {
                'total_respostas': total_respostas,
                'nps_medio': round(float(nps_medio), 2),
                'problemas': {
                    'resolvidos': problemas_sim,
                    'nao_resolvidos': problemas_nao,
                    'taxa_resolucao': round((problemas_sim / total_respostas * 100), 2) if total_respostas > 0 else 0
                },
                'nps_distribuicao': {
                    'detratores': detratores,
                    'neutros': neutros,
                    'promotores': promotores
                },
                'consultores': [{
                    'nome': c.consultor,
                    'total_atendimentos': c.total,
                    'nps_medio': round(float(c.nps_medio), 2) if c.nps_medio else 0
                } for c in consultores]
            }
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/v1/export/excel', methods=['GET'])
def api_v1_export_excel():
    """Exportar todas as respostas para arquivo Excel"""
    try:
        respostas = Resposta.query.order_by(Resposta.data_resposta.desc()).all()
        
        # Criar DataFrame com pandas
        dados = [{
            'ID': r.id,
            'Email': r.email,
            'Data Visita': r.data_visita,
            'Placa': r.placa,
            'Consultor': r.consultor,
            'Motivo Visita': r.motivo_visita,
            'Problema Resolvido': r.problema_resolvido,
            'Problema Não Resolvido': r.problema_nao_resolvido,
            'Sugestões': r.sugestoes,
            'NPS (0-10)': r.probability,
            'Data Resposta': r.data_resposta.strftime('%Y-%m-%d %H:%M:%S')
        } for r in respostas]
        
        df = pd.DataFrame(dados)
        
        # Criar arquivo Excel em memória
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='Respostas', index=False)
        
        output.seek(0)
        
        # Gerar nome do arquivo com timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'pesquisa_satisfacao_{timestamp}.xlsx'
        
        return send_file(
            output,
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            as_attachment=True,
            download_name=filename
        )
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
