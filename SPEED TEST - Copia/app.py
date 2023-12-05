from flask import Flask, render_template, request, jsonify
from datetime import datetime
from flask_cors import CORS
import speedtest

app = Flask(__name__)
CORS(app)

historico = []

@app.route('/')
def index():
    return render_template('index.html', historico=historico)

@app.route('/historico')
def obter_historico():
    return jsonify(historico)

@app.route('/adicionar-ao-historico', methods=['POST'])
def adicionar_ao_historico():
    dados = request.get_json()
    velocidade_download = dados['velocidade_download']
    velocidade_upload = dados['velocidade_upload']
    data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    teste = {'data_hora': data_hora, 'velocidade_download': velocidade_download, 'velocidade_upload': velocidade_upload}
    historico.append(teste)
    return jsonify({'status': 'ok'})

@app.route('/speedtest')
def testar_velocidade():
    st = speedtest.Speedtest()
    velocidade_download = st.download()
    velocidade_upload = st.upload()
    return jsonify({'velocidade_download': velocidade_download, 'velocidade_upload': velocidade_upload})

if __name__ == '__main__':
    app.run(debug=True)
