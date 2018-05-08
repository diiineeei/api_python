import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config.email import EMAIL


class EnviaEmail:

    @staticmethod
    def enviar_email(destinatario, dados, titulo):
        msg = MIMEMultipart('alternative')
        msg['Subject'] = titulo
        msg['From'] = EMAIL["remetente"]
        msg['To'] = destinatario
        html = EnviaEmail.monta_html(dados)
        part = MIMEText(html, 'html')
        msg.attach(part)
        s = smtplib.SMTP(EMAIL['smtp'])
        s.starttls()
        s.login(EMAIL['usuario'], EMAIL['senha'])
        s.sendmail(EMAIL['remetente'], destinatario, msg.as_string())
        s.quit()

    @staticmethod
    def monta_html(dados):
        html = EnviaEmail.inicio_html()
        html += "<p><strong>" + dados + "</strong></p>"
        html += EnviaEmail.fim_html()
        return html

    @staticmethod
    def inicio_html():
        return """
        <table width="100%" cellspacing="0" cellpadding="0" border="0">
        <tbody>
        <tr>
        <td style="padding:20px; color:#4A423C; font-family:arial,helvetica,sans-serif; font-size:16px">
        <p style="text-align:justify">
        <span style="font-size:24px">
        <strong>E-mail Enviado pela api em python</strong>
        </span>
        </p>"""

    @staticmethod
    def fim_html():
        return """</ul><p style="text-align:center"><span style="font-size:18px">
        <strong>Powered by: Rodinei Lima</strong></span></p>
        </td>
        </tr>
        </tbody>
        </table>"""
