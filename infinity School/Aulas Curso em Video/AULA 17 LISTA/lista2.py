valores = list()
valores.append(5)
valores.append(9)
valores.append(2)

for p, v in enumerate(valores):
    print(f"Na posição {p} encontrei o valor {v}")
print("Cheguei ao final da lista")


a = [2,3,4,7]
b = a [:] # receber todos os itens de A (copia dos valores)
b[2] = 8

print(f"Lista A: {a}")
print(f"Lista A: {b}")