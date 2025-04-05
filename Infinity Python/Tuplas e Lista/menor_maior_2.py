"Faça um programa que leia 5 valores numericos e guarde-os em uma lista, no final mostre qual foi o maior e menor valor digitado e suas respectivas posições na lista"

# prmeiro: armazena todos os numeros na lista

valores = []

for v in range(5):
    n1 = float(input(f"Digite o {v+1}ª número: "))
    valores.append(n1)

# segundo: pegar o primeiro valor da lista
primeiro_valor = valores[0]

maior_elemento = max(valores)
menor_elemento = min(valores)

print(f" O maior número é {maior_elemento}")
print(f" O menor número é {menor_elemento}")