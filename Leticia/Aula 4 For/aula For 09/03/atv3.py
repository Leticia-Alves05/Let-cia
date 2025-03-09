"""Ex03. Faça um programa que peça 5 numeros para o usuário
e mostre o maior numero inserido."""

maior_numero = 0 

for n in range(5):
    numero=int(input(f"Digite o {n+1} numero: "))
    if numero > maior_numero:
        maior_numero = numero

        
print(maior_numero)