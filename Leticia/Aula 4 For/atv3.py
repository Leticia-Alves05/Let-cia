"""Faça um programa onde o usuário irá fazer uma contagem
e ele irá informar o Inicio, o Final e o Passo da contagem."""

inicio = int(input(" Digite um número: "))
final = int(input(" Digite um número: "))
passo = int(input(" Digite um número: "))

for i in range(inicio,final+1,passo):
    print(i)