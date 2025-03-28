lista = ("doces", 25.40, "salgados", 102.60, "bebidas", 80.20)

print("-" * 40)
print("LISTA DE PREÇOS")
print("-" * 40)

for pos in range(0,len(lista)):
    if pos % 2 == 0:
        print(f"{lista[pos]:.<30}" , end=" ")
    else:
        print(f"R${lista[pos]:>7.2f}")

