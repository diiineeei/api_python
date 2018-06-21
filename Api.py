from service.api_service import ApiService
from flask import Flask, request
from config.api import API
import logging


app = Flask(__name__)
file_handler = logging.FileHandler('app.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)


@app.route('/', methods=['GET'])
def get():
    app.logger.warning('info : consultando cadastro')
    return ApiService().get()


@app.route('/cadastro', methods=['POST'])
def cadastro():
    app.logger.warning('info : cadastrando')
    return ApiService().post_cadastro(request.headers)


@app.route('/http_cats', methods=['GET'])
def http_cats():
    app.logger.warning('info : consultando http_cats')
    return ApiService().http_cats(request.headers)


@app.route('/delete/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    app.logger.warning('info : usado delete')
    return ApiService.delete(task_id)


if __name__ == '__main__':
    app.run(host=str(API["host"]), debug=bool(API["debug"]), port=int(API["port"]))
