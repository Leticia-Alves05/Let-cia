
pessoas = []


while True:
    dado = []
    dado.append(input("Digite seu nome: "))
    dado.append(float(input("Digite seu peso: ")))
    pessoas.append(dado)
    #pessoas.append(dado[:])
    #dado.clear()
    resposta = input("Deseja continuar? [S/N]  ")
    if resposta in "Nn":
        break

pessoas_mais_pesadas = []
maior_peso = 0
for n, p in pessoas:
    if p > maior_peso:
        maior_peso = p
        pessoas_mais_pesadas.clear
        pessoas_mais_pesadas.append(n)
    elif p == maior_peso:
        pessoas_mais_pesadas.append(n)
        



print(f" Existe {len(pessoas)} pessoas")






print(f"{pessoas}")

# [ana, 55]
# [joao, 70]
# pessoas = [[ana, 55], [joao, 70]]
