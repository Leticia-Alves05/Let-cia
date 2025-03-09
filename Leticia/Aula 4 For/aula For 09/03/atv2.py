"""Ex02. Você está fazendo um programa para calcular médias.
O programa deve solicitar ao usuário a quantidade de numeros
e depois pedir essa quantidade.
Ao final, mostre a média dos numeros inseridos."""

media = 0

contagem = int(input("Digite um numero: "))
soma = 0

for i in range(contagem):
    numero = int(input(f"Digite o {i+1} número:"))
    soma += numero
    

media = soma / contagem

print(f"A media dos números é: {media}")



