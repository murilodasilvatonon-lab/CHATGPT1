print("Bem vindo ao portal Educacional do Murilo.")

notaUm = float(input("Digite a primeira nota do aluno: "))
notaDois = float(input("Digite a segunda nota do aluno: "))
notaTres = float(input("Digite a terceira nota do aluno: "))
notaQuatro = float(input("Digite a quarta nota do aluno: "))

media = (notaUm + notaDois + notaTres + notaQuatro) / 4

print(f"A média é {media}")

if media >= 6:
    print("Parabéns! Você está aprovado!")
else:
    print("Você está reprovado! Estude mais ano que vem!")