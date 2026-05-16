#Instalar bibliotecas
# ">" = Codigo
# > pip install requests

#Segundo passo: adicionar/importar ao codigo
import requests

url = "https://viacep.com.br/ws/13473720/json/"

dados = requests.get(url).json()

print(dados)

##############################

cep = input("Qual seu cep? ")

