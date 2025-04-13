def saudacao(nome = " "):
    if nome == " ":
        return "Olá"
    else:
        return (f"Olá {nome}")
    




    

nome = input("Digite seu nome: ")
mensagem = saudacao(nome)
print(mensagem)