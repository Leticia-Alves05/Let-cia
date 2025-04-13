"Faça um programa que peça o nome e 3 notas de um aluno, essas informações devem ser salvas em um dicionário com as chaves 'nome' e 'notas' (notas deve ser uma lista com as 3 notas)."
"Depois, calcule a média do aluno e sua situação (APROVADO se a nota for maior ou igual a 6, se não reprovado) e armazene essas informações em 2 novas chaves"
"Ao final mostre todas as informações do aluno."

aluno = {}

aluno["nome"] = input("Digite o nome do aluno: ")
aluno['notas'] = []

# obtendo as notas
for n in range(3):
    nota = float(input(f"Digite sua {n+1}º nota: "))
    aluno['notas'].append(nota) #atribuindo as notas dentro do dicionario

 

aluno['media'] = sum(aluno['notas']) / len(aluno['notas']) # sum =  soma 
aluno['situcao'] = 'APROVADO' if aluno['media'] >= 6 else 'REPROVADO'

print(" Dados do Aluno")
for chave, valor in aluno.items(): 
    print(f"{chave.capitalize()}: {valor}") # capitalize =  primeira letra maiuscula





