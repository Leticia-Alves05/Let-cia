

numero_alunos = int(input("Digite o número de alunos: "))

for numero in range(1,numero_alunos+1):
    nome = (input("Digite seu nome: "))
    n1 = float(input("Digite sua 1º nota: "))
    n2 = float(input("Digite sua 2º nota: "))
    n3 = float(input("Digite sua 3º nota: "))
    media = (n1 + n2 + n3) / 3
    media_aluno = media 
    if media_aluno >= 7.0:
        print(f"{nome}, suas notas são: {n1},{n2},{n3} sua media é de: {media_aluno}. Parabéns você esta aprovado")
    else:
        print(f"{nome}, suas notas são: {n1},{n2},{n3} sua media é de: {media_aluno}. Você esta reprovado")



