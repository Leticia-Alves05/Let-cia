"Faça um programa que peça o nome e 3 notas de um aluno, essas informações devem ser salvas em um dicionário com as chaves 'nome' e 'notas' (notas deve ser uma lista com as 3 notas)."
"Depois, calcule a média do aluno e sua situação (APROVADO se a nota for maior ou igual a 6, se não reprovado) e armazene essas informações em 2 novas chaves"
"Ao final mostre todas as informações do aluno."

aluno = {}
notas = []
soma = 0

aluno["nome"] = input("Digite seu nome: ")

# obtendo as notas
for n in range(3):
    nota = int(input(f"Digite sua {n+1}º nota: "))
    notas.append(nota)
    soma += nota

# calculando a soma
#for nota in notas:
#    soma += nota

print(aluno)
print(f"Suas notas foram: {notas}")


media = soma / 3
if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")