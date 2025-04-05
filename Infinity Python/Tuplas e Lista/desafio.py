
"Vocês foram contratados para Desenvolver um sistema para registrar vendas de uma loja de doce:"

"- Ao funcionario chegar na loja, ele inicia o sistema que fica rodando durante todo o expediente (ou seja, em processo de repetição)"

"- Ao registrar uma venda, o sistema pede: nome do cliente, endereco do cliente, numero de telefone do cliente e valor da compra. Essas informações precisam ser armazenadas de alguma forma (fica a criterio de vocês descobrir como armazenar essas informações)"

"- Após cada venda registrada, o sistema perguntará se o operador deseja registrar outra venda, e caso não queira encerra o programa."

"- Ao encerrar o programa, o sistema sorteia uma das vendas do dia para enviar um brinde para o cliente sorteado (fica ao seu criterio entender como fazer o sorteio)"

from random import randint
lista_de_vendas = []

while True:
    nome = (input("Digite seu nome: "))
    cep = int(input("Digite seu CEP: "))
    numero = int(input("Digite seu número: "))
    valor_da_compra = float(input("Valor da compra: "))

    venda = nome,cep,numero,valor_da_compra
    lista_de_vendas.append(venda)

    registro = (input("Deseja registrar outra venda? [S/N]"))
    while registro != "N" and registro != "S":
        registro = (input("Deseja registrar outra venda? [S/N]"))
        
    if registro.upper() == "N": 
        break
    else: 
        print("Continue")

numero_de_vendas = len(lista_de_vendas)
numero_sorteado = randint(0,numero_de_vendas-1)

venda_ganhadora = lista_de_vendas[numero_sorteado]

print(venda_ganhadora)
#(nome, cep, numero, valordacompra)