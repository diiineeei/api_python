# README #

### Para que é esse repositório? ###

Demonstrar como funciona uma Api em python

### Como faço para configurar? ###
A configuração é feita ultilizando o pip instalando as dependencias do arquivo requirements.txt
também se faz necessario a instalação la biblioteca libnss3-tools

Deve-se configurar os arquivos da pasta config/*.dist, para que o programa envie emails, acesse o banco de dados e execute a Api.

##### Exemplo arquivo email.py: #####
```
EMAIL = {
   "remetente": "remetente@empresa.com",
   "smtp": "smtp.empresa.com.br:587",
   "usuario": "user@empresa.com.br",
   "senha": "senha@2017"
}
```

##### Exemplo arquivo api.py: #####
```
API = {
   "host": "192.168.0.2",
   "port": "8000",
   "debug": "1"
}
```