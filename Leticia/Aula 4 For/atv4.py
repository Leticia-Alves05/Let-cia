qtd_vogais = 0


print("Contador de vogais")
texto = input("Digite uma palavra: ")

for letra in texto:
   #letra = letra.upper() in ("A", "E" , "I", "O", "U")
   if letra.upper() in "AEIOU":
      qtd_vogais += 1 

print(f"A quantidade de vogais é:{qtd_vogais}")
    


