import requests

cep = input("Qual seu cep? ")

url = f"https://viacep.com.br/ws/{cep}/json/"

dados1 = requests.get(url)

dadosfinal = dados1.json()

print(dadosfinal)