from service.envia_email import EnviaEmail


class ApiService:

    @staticmethod
    def nao_autorizado():
        return "<p>401 Unauthorized</p><p>The request requires user authentication</p>", 401

    @staticmethod
    def send_email(email, msg, titulo):
        EnviaEmail.enviar_email(email, msg, titulo)
        return "Email enviado com sucesso!", 200
