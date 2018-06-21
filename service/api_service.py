from flask import request, jsonify, abort
from flask import abort


class ApiService:

    @staticmethod
    def get():
        response = jsonify({
                    'id': "001",
                    'name': "Rodinei Lima",
                    'date_created': "11/11/2017",
                    'date_modified': "20/05/2018"
                })
        response.status_code = 200
        return response

    @staticmethod
    def post_cadastro(headers):
        try:
            response = jsonify({
                'id': headers["id"],
                'name': headers["name"],
                'date_created': headers["date_created"],
                'date_modified': headers["date_modified"]
            })
            response.status_code = 201
            return response
        except KeyError:
            return "Acesso negado/proibido", 403

    @staticmethod
    def http_cats(headers):
        try:
            response = '''
            <html>
                <head>
                    <meta name="viewport" content="width=device-width, minimum-scale=0.1">
                </head>
                <body style="margin: 0px; background: #0e0e0e;">
                    <img style="-webkit-user-select: none;" src="https://http.cat/''' + str(headers["http"]) + '''.jpg"</img>
                </body>
            </html>'''
            return response, headers["http"]
        except KeyError:
            response = '''
                        <html>
                            <head>
                                <meta name="viewport" content="width=device-width, minimum-scale=0.1">
                            </head>
                            <body style="margin: 0px; background: #0e0e0e;">
                                <img style="-webkit-user-select: none;" src="https://http.cat/404.jpg"</img>
                            </body>
                        </html>'''
            return response, 404

    @staticmethod
    def delete(task_id):
        tasks = [
            {
                'id': 1,
                'title': u'Buy groceries',
                'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
                'done': False
            },
            {
                'id': 2,
                'title': u'Learn Python',
                'description': u'Need to find a good Python tutorial on the web',
                'done': False
            }
        ]
        task = [task for task in tasks if task['id'] == task_id]
        if len(task) == 0:
            abort(404)
        tasks.remove(task[0])
        return jsonify({'result': True})
