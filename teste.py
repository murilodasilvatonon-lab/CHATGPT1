import requests

#colhe o cep
nome = input("Digite seu nome: ")
email = input("Digite seu e-mail: ")
telefone = input("Digite seu telefone: ")
cep = input("Qual seu cep? ")

#cria uma variael e atribui o resultado do link
#Utilizamos o f string, para conseguir inserir uma variavel
url = f"https://viacep.com.br/ws/{cep}/json/"

dados = requests.get(url).json()

print(f"Bem vindo ao Mercado Libre {nome}! o seu e-mail é {email}. O seu telefone é {telefone}. você mora na rua {dados['logradouro']}, na cidade {dados['localidade']}, no estado de {dados['estado']}.") 

#atribuindo variaveis para cada um dos resultados
# rua = dados['logradouro']
# bairro = dados['bairro']
# cidade = dados['localidade']

# bairro = dados

# print(rua)
# print(bairro)
# print(cidade)