
#Faça um Programa que Peça 3 Notas, Ao final, mostre as notas e a média entre elas.
notas = []


# Preenchimento da Lista
for n in range(3):
    nota = float(input(f'Digite a {n+1}ª nota: '))
    notas.append(nota)

# Mostrar os Elementos da Lista
# 1º 
# qtd_notas = len(notas)

# print('Notas:')
# for n in range(qtd_notas):
#     print(f'- {notas[n]:.2f}')

# 2º
print("Notas: ")
for nota in notas:
    print(f'- {nota:.2f}')

media = sum(notas)/ len(notas)
print(f" Á media das notas é: {media:.2f}")