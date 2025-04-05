"Faça um programa que leia 5 valores numericos e guarde-os em uma lista, no final mostre qual foi o maior e menor valor digitado e suas respectivas posições na lista"


valores = []

primeiro_valor = float(input(f"Digite o número para a posição {0} "))
valores.append(primeiro_valor)
maior_valor = primeiro_valor
menor_valor = primeiro_valor

for v in range(1,5):
   n1 = float(input(f"Digite o número para a posição {v} "))
   valores.append(n1)
   if n1 > maior_valor:
      maior_valor = n1
   if n1 < menor_valor:
      menor_valor = n1

 


print(f"{valores}")

print(f"O maior valor é {maior_valor}")
print(f"O menor valor é {menor_valor}")
    
