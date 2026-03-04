"Faça um programa que pede um numero para o usuario, e mostre o enesimo valor da sequancia de fibonacci. Exemplo: "
"Ate qual numero deseja mostrar finonacci?"
">>>8"
"0 1 1 2 3 5 8 13"
"OBS a sequencia de fibonacci começa com 0 e 1 e o proximo termo é a soma dos dois anteriores."


#t1 = 0 # numerp_atual
#t2 = 1 #sucessor
#aux = None # antecessor

#n = int(input("Digite ate qual número deseja mostrar a sequência: "))

#for _ in range(n):
   # print(t1, end=" ") #t1, t2 = t2, t1 + t2
    #aux = t2 #antecessor =  sucessor
    #t2 = t1 + t2 # sucessor = numero_atual + sucessor 
    #t1 = aux # numero_atual = antecessor

#print("\n")



n = int(input("Digite ate qual número deseja mostrar a sequência: "))

antecessor = 0 
sucessor = 1 

for _ in range(n):
    print(antecessor, end=" ")
    antecessor, sucessor = (sucessor, antecessor + sucessor)

    print("\n")