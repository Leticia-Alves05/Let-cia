"Faça uma função calcular_media onde ela deve receber 3 notas e retornar a média entre as notas."

def media(i):
    return (i)/3

soma = 0 

for i in range(3):
    n1 = int(input("Digite o primeiro número: "))
    soma = soma + i



resultado = media(i)

print(f"A média dos número é : {resultado}")
