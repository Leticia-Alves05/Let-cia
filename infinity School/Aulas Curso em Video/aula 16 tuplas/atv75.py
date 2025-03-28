num = (int(input("Digite um número: ")),int(input("Digite um número: ")),int(input("Digite um número: ")),int(input("Digite um número: ")))

print(f"Você digitou os valores {num}")

print(f" o numero nove apareceu {num.count(9)} vezes. ")

if 3 in num:
        print(f"O número 3 está na  {num.index(3)+1}ª posição")
else:
        print("Não consta o número 3 ")
    
print("Os valores pares digitados foram: ")
for n in num:
    if n % 2 == 0:
        print(n)