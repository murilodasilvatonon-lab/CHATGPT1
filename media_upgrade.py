listanotas = []

print("-" * 40)
print("Bem vindo a I.A que calcula notas e média final 🤖🔢")
print("-" * 40)

while True:
    notas = input("Digite a nota que deseja inserir (digite sair para parar): ")
    
    if notas.lower() == "sair": #Comando lower obriga a entrada ser toda minuscula
        break
    else:
        listanotas.append(float(notas)) #insere dados em uma lista
        
media = sum(listanotas) / len(listanotas)

print(f"A média final do aluno é {media:.2f}")