idade = int(input(' Digite sua idade: '))
if idade < 16:
    print(" Não pode votar")
elif 18 > idade >= 16:
    print("voto facultativo")
elif 18 <= idade < 65:
    print("voto obrigatorio")
else:
    print("voto facultativo")