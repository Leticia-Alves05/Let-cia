"[-2] conta de tras pra frente ex: -1 pudim e -2 é pizza"
"[1:3] conta do elemento 1 ate o 3 mas elimina o numero 3 ex: imprimi suco e pizza"
"[2:] conta do 2 ate o final ex; pizza e pudim"
"[:2] conta do inicio ate o 2 mas ignora o 2 ex: hamburguer e suco"
"[-2:] ele começa no 2- e vai ate o final"
#Tuplas são imutaveis

lanche = "hamburguer" , "suco", "pizza", "pudim", "batata frita"
#print(lanche[0])

#for comida in lanche:
   # print(f" Eu vou comer {comida}")

for cont in range(0, len(lanche)):
   print (f"Eu vou comer {lanche[cont]} na posição {cont}")



print(sorted(lanche)) #imprimi em ordem alfabetica

a = (2,5,4)
b = (5,8,1,2)
c = b + a
print(c)
print(c.count(5)) # quantas vezes aparece o 5
print(c.index(4)) # qual posição esta o nº 4