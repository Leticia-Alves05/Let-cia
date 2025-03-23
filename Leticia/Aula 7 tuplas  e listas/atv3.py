"Faça um programa que peça 6 numeros e armazene-os em uma lista. Ao final, mostre a soma entre os numeros."
soma = 0
lista=[]

for n in range(6):
    numero = float(input("Digite um número: "))
    lista.append(numero)

for s in lista:
    soma += s

print(soma)