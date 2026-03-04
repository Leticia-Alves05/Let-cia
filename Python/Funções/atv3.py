"Ex03. A função deve receber uma lista de notas e retornar a média das notas"

def media(lista):
    media = sum(lista) / len(lista)
    return media

notas = []

for i in range(3):
    nota = int(input("Digite um número: "))
    notas.append(nota)



print(media(notas))

