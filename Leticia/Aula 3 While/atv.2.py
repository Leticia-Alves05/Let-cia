#Faça um programa que peça um numero positivo para o usuário, e realize uma contagem de 1 até esse numero (ele incluso).

contador = 1
numero = int(input("Digite um número: "))

while contador <= numero:
    print(contador)
    contador += 1

print("Fim do Programa")
