#Você está criando um programa em Python para simular um jogo simples de adivinhação. O programa deve ter um número fixo, por exemplo, 7, que o jogador deve adivinhar. O jogador terá até 3 tentativas para acertar o número. Implemente o jogo utilizando um loop while para permitir que o jogador faça múltiplas tentativas até acertar ou atingir o limite de tentativas. Utilize a estrutura else para exibir uma mensagem de encorajamento caso o jogador acerte e uma mensagem de consolo caso as 3 tentativas se esgotem sem sucesso.

print("Jogo de Adivinhação: Tente adivinhar o número entre 1 a 10")

numero_de_tentativas = 3

while numero_de_tentativas != 0: # enquato
    numero = int(input('Digite um número de 1 a 10: '))
    if numero == 5:
        print(f"Parabens voce acertou - {numero}")
        break
    else:
        print("Não foi dessa vez")
        numero_de_tentativas -= 1

if numero_de_tentativas == 0:
    print("Nao fique triste, tente de novo e na proxima voce vai conseguir")



