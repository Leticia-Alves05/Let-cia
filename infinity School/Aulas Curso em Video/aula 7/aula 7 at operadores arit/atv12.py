preço = float(input(" Digite o preço do produto: "))

valor = (preço * 5) / 100
novo_preço = preço - valor

print(f"O preço com desconto é de R${novo_preço}.")