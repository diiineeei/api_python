from service.api_service import ApiService
from flask import Flask, request
from config.api import API
import logging

app = Flask(__name__)
file_handler = logging.FileHandler('app.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)


@app.route('/', methods=['GET'])
def nao_autorizado():
    app.logger.warning('warning : Tentativa de acesso ao /')
    return ApiService().nao_autorizado()


@app.route('/email', methods=['POST'])
def send_email():
    try:
        email = str(request.headers['email'])
        titulo = str(request.headers['titulo'])
        msg = str(request.headers['msg'])
        app.logger.info('info : Email enviado para ' + str(email))
        return ApiService().send_email(email, msg, titulo)
    except KeyError:
        app.logger.warning('warning : Acesso proibido sem Header solicitado!')
        return "Acesso negado/proibido", 403


if __name__ == '__main__':
    app.run(host=str(API["host"]), debug=bool(API["debug"]), port=int(API["port"]))
