#Primeiro: Instalar bibliotecas 
#pip install requests

#Segundo passo: adicionar/importar ao código
import requests

nome = input("Digite o seu nome: ")
email = input("Digite o seu e-mail: ")
telefone = input("Digite o seu telefone: ")
#Recebe o CEP digitado pelo usuário
cep = input("Digite o seu CEP: ")


#Cria uma variável e atribui o resultado do link
#Utilizamos o f string, para conseguir inserir uma variável no link
url = f"https://viacep.com.br/ws/{cep}/json/"

dados = requests.get(url).json()

print(f"Bem vindo ao Mercado Livre {nome}! O seu e-mail é {email}.O seu telefone é {telefone}. Você mora na rua {dados['logradouro']}, na cidade {dados['localidade']}, no estado de {dados['estado']}.")

#Atribuindo variáveis para cada um dos resultados
# rua = dados['logradouro']
# bairro = dados['bairro']
# cidade = dados['localidade']

# print(rua)
# print(bairro)
# print(cidade)




