#Faça um programa que peça uma quantidade indeterminada de numeros e pare quando o usuário pedir um numero negativo. 
# Ao final mostre a soma dos numeros desconsiderando o numero de parada (o negativo).

soma = 0

while True:
    numero = float(input("Digite um número: "))
    if numero >= 0:
        soma += numero
    else:
        break
print(soma)