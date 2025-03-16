"Fça um programa que peça um numero e informe se esse numero é primo ou não.""OSB: Lembrando que um numero primo é divisil por 1 e por ele mesmo"

# verificarse é um numero primo: 
# se no intervalo de 1 - n tiver 2 divisores
# se no intervalo de 2 - n-1 não encontrar divisores

#qtd_divisores = 0 
#num = int(input("Digite um número: "))

#for n in range(1, num + 1):
 #   if num % n == 0:
  #      qtd_divisores += 1

#if qtd_divisores == 2:
 #   print("O numero é primo.")
#else:
#    print ("o numero não é primo")



num = int(input("Digite um número: "))
primo = num > 1

for n in range(2,num):
    if num % n == 0 :
        primo = False
        break

if primo:
    print ("O numero é primo")

else:
    print ("O número não é primo")
