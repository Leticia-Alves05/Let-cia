" Faça um programa que peça um texto para o usuário e crie um dicionário que irá conter todas as letras e suas respectivas quantidades, exemplo:"


letras = {}
texto = input("Digite uma palavra: ")



for caractere in texto:
    if caractere == " ": # continua se tiver espaço , como por exemplo se o usuario digitar frase
        continue

    caractere = caractere.lower() # padronizando tudo para minusculo 
    if letras.get(caractere) == None:
        letras[caractere] = 1
    else:
        letras[caractere] += 1 



print(letras)


