##Faça um programa que peça varios numeros, e após cada numero pergunte se o usuário deseja continuar (ele deve responder 'S' para Sim e 'N' para Não), 
# quando essa resposta for 'N' você deve parar a repetição e mostrar a média dos numeros digitados.

qtd_numero = 0
soma_numeros = 0
decisao_do_usuario = 'S' 

while decisao_do_usuario == "S":
    numero_do_usuario = int(input("Digite um número: "))
    qtd_numero += 1
    soma_numeros += numero_do_usuario
    decisao_do_usuario = str(input("Deseja continuar: "))
    if decisao_do_usuario == "N":
        break

media = soma_numeros / qtd_numero
print(f"{media}")
