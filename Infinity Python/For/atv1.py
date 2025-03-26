"Você está desenvolvendo um programa em Python para calcular a soma dos números pares dentro de um intervalo determinado pelo usuário. O programa deve solicitar ao usuário que insira dois números inteiros, representando o início e o fim do intervalo (inclusive). Utilize um loop 'for' para iterar sobre todos os números no intervalo e somar apenas os números pares. Implemente a estrutura 'else' para exibir uma mensagem indicando que não há números pares no intervalo, caso seja o caso. Ao final, exiba a soma dos números pares encontrados"

qtd_num_par = 0
soma = 0

inicio_intervalo = int(input("Digite um número: "))
fim_intervalo = int(input("Digite outro número: "))

for numero in range(inicio_intervalo,fim_intervalo):
    if numero % 2 == 0:
        print(f"{numero}")
        soma += numero
        qtd_num_par +=1 

if qtd_num_par == 0:
    print("Não há números pares no intervalo")

print(f"A soma dos números é {soma}")