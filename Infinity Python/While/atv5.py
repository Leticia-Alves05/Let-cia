##Faça um programa que peça varios numeros, e após cada numero pergunte se o usuário deseja continuar (ele deve responder 'S' para Sim e 'N' para Não), 
# quando essa resposta for 'N' você deve parar a repetição e mostrar a média dos numeros digitados.

# media = soma_total / quantidade_de_numeros
decisao_do_usuario = "S" # "N"
soma_total_dos_numeros = 0
quantidade_de_numero = 0

while True:
    numero_do_usuario = int(input("Digite um numero: "))
    quantidade_de_numero += 1 # quantos numeros
    soma_total_dos_numeros += numero_do_usuario
    decisao_do_usuario = str(input("Deseja continuar: "))

    while decisao_do_usuario != "S" and decisao_do_usuario != "N":
        print("Digite S ou N")
        decisao_do_usuario = str(input("Deseja continuar: "))

    if decisao_do_usuario == "N":
        break

media = soma_total_dos_numeros / quantidade_de_numero
print(f"Media: {media}")
