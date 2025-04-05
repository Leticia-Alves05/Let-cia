"crie um programa onde o usuario possa digitar varios valores numericos e cadastre-os em uma lista, caso o numero já exista la dentro, ele não sera adicionado. No final serão exibidos todos os valores unicos digitados em ordem crescente"

valores_numericos = []

while True:
    valores_numericos.append(float(input("Digite um número: ")))
    valores_numericos.append(float(input("Digite o proximo número: ")))
    for pos in range(0, len(valores_numericos)):
        print(f"")