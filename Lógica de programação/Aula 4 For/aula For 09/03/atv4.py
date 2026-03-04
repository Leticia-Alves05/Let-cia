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
menor_numero = float("inf")
maior_numero = float("-inf")
media_dos_numeros = 0
soma = 0

while True:
    numero = float(input("Digite um número: "))

    soma += numero
    qtd_numero += 1

    if numero > maior_numero:
        maior_numero = numero

    if numero < menor_numero:
        menor_numero = numero

    resp =input("Deseja continuar? [S/N]")
    if resp.upper()=="N":
        break

media = soma / qtd_numero

print(f"Quantidade de número digitados foi:{qtd_numero}")
print(f"Maior número digitado foi:{maior_numero}")
print(f"Menor número digitado foi:{menor_numero}")
print(f"A soma dos números digitados é:{soma}")
print(f"A media dos números digitados é:{media}")
    
print("Fim do programa.")    