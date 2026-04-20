from flask import Flask, request, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
import urllib.parse
import requests

# 1. Configuração do App 
base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, 
            static_folder=base_dir, 
            static_url_path='')

# 2. Configuração do Banco de Dados
uri = os.environ.get("DATABASE_URL", "sqlite:///pesquisa.db")
if uri and uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 3. Credenciais
ADMIN_CREDENTIALS = {
    'email': 'admin@vwcapivari.com',
    'password': 'admin'
}

# 4. Modelo do Banco
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

# 5. Rota Principal 
@app.route('/')
def home():
    # Força a busca no diretório base
    return send_from_directory(base_dir, 'tela_login.html')

# 6. Função de WhatsApp 
def enviar_alerta_whatsapp(placa, consultor, problema_nao_resolvido, probabilidade):
    telefone_gerente = "5519989288856"  
    api_key = "6073595" 
    
    mensagem = (
        f"🚨 *ALERTA DE CLIENTE INSATISFEITO* 🚨\n\n"
        f"🚗 *Placa:* {placa}\n"
        f"👨‍💼 *Consultor:* {consultor}\n"
        f"❌ *Problema:* {problema_nao_resolvido if problema_nao_resolvido else 'Não especificado'}\n"
        f"📉 *Chance de retorno:* {probabilidade}%\n\n"
        f"Por favor, verifique a situação imediatamente!"
    )
    
    mensagem_codificada = urllib.parse.quote(mensagem)
    url = f"https://api.callmebot.com/whatsapp.php?phone={telefone_gerente}&text={mensagem_codificada}&apikey={api_key}"
    
    try:
        requests.get(url, timeout=10) # Adicionado timeout para não travar o site
    except Exception as e:
        print(f"Erro WhatsApp: {e}")

# 7. Inicialização do Banco (Segura para Nuvem)
with app.app_context():
    # create_all() não apaga dados existentes, apenas cria o que falta
    db.create_all()

# --- OUTRAS ROTAS ---

@app.route('/submit', methods=['POST'])
def submit():
    try:
        email = request.form.get('email', '')
        data_visita = request.form.get('date')
        placa = request.form.get('plate')
        consultor = request.form.get('consultant')
        motivo_visita = request.form.get('reason')
        problema_resolvido = request.form.get('resolved')
        problema_nao_resolvido = request.form.get('unresolved_reason', '')
        sugestoes = request.form.get('suggestions', '')
        
        try:
            probability = int(request.form.get('probability', 0))
        except:
            probability = 0

        nova_resposta = Resposta(
            email=email, data_visita=data_visita, placa=placa,
            consultor=consultor, motivo_visita=motivo_visita,
            problema_resolvido=problema_resolvido,
            problema_nao_resolvido=problema_nao_resolvido,
            sugestoes=sugestoes, probability=probability
        )

        db.session.add(nova_resposta)
        db.session.commit()

        if problema_resolvido == 'Não' or probability <= 50:
            enviar_alerta_whatsapp(placa, consultor, problema_nao_resolvido, probability)
            
        return jsonify({'success': True}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/admin/login', methods=['POST'])
def admin_login():
    data = request.get_json()
    if data.get('email') == ADMIN_CREDENTIALS['email'] and data.get('password') == ADMIN_CREDENTIALS['password']:
        return jsonify({'success': True}), 200
    return jsonify({'success': False}), 401

@app.route('/admin/respostas', methods=['GET'])
def get_respostas():
    respostas = Resposta.query.order_by(Resposta.data_resposta.desc()).all()
    return jsonify([{
        'id': r.id, 'placa': r.placa, 'consultor': r.consultor,
        'probability': r.probability, 'data_resposta': r.data_resposta.strftime('%d/%m %H:%M')
    } for r in respostas])

# Rota para carregar arquivos CSS, JS e Imagens automaticamente
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    # Porta dinâmica para o Railway
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)