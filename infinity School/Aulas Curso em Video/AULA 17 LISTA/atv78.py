valores = []
maior_valor = 0
menor_valor = 0


for v in range(5):
    valores.append(float(input(f"Digite o {v + 1}ª número: ")))
    if v > maior_valor:
         maior_valor = valores[v] 
    if v < menor_valor:
         menor_valor = valores[v]


print(f"{valores}")

print(f"O maior valor é {maior_valor}")
print(f"O menor valor é {menor_valor}")



