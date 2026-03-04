"02. Faça um programa que peça 5 nomes e mostre todos os nomes digitados"

lista=[]

for n in range(5):
    nome = (input(f"Digite o {n+1} nome: "))
    lista.append(nome)

print(f'{lista}')

print("Nomes: ")
for nome in lista:
    print(f"-> {nome}")
