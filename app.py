print("-" * 50)
print("Bem vindo ao coletor de dados do ChatGPT 🤖")
print("-" * 50)

#colhe as informacoes
nome = input("Digite o seu nome: ")
email = input("Digite o seu email: ") # variavel para armazenar email do usuario
cidade = input("Digite a sua cidade: ")
estado = input("Digite o seu estado: ")
pais = input("Digite o seu país: ")
nascimento = int(input("Digite o ano que voce nasceu: "))
anoatual = int(input("Digite o ano que voce esta: "))
idadeatual = anoatual - nascimento
# idadeatual = int(input("Digite a sua idade: "))
# idadefutura = idadeatual + 1


#exibi as informacoes
print(f"Olá {nome}! O seu e-mail é {email}, Você mora em {cidade}, {estado} - {pais} e você tem {idadeatual} anos.")