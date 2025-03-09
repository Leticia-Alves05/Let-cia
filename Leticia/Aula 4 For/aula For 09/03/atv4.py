"""Faça um programa que peça uma quantidade indeterminada
de numeros para o usuário, após cada numero 
pergunte "Deseja continuar? [S/N]".
Quando o usuário encerrar, mostre:
- Quantidade de Numeros Inseridos
- Menor Numero
- Maior Numero
- Soma dos Numeros
- Média dos Numeros
"""

qtd_numero = 0 
menor_numero = 0
maior_numero = 0
media_dos_numeros = 0

while True:
    numero = float(input("Digite um número: (ou S para parar)"))
    if numero.lower()== "s": 
        break
    