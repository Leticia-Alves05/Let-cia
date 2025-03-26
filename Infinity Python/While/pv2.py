"Crie um programa em Python que simule um sistema de login. O programa deve permitir ao usuário três tentativas para acertar o nome de usuário e a senha corretos. Caso o usuário erre as credenciais, o programa deve fornecer uma mensagem informando quantas tentativas restam. Se o usuário acertar, uma mensagem de boas-vindas deve ser exibida, e o programa deve terminar imediatamente."
"Se todas as três tentativas falharem, o programa deve usar um loop for para exibir uma mensagem de: Acesso bloqueado repetida três vezes."


numero_de_tentativa = 3


for t in range(3):
    login = int(input('Digite o login: '))
    senha = int(input("Digite sua senha: "))
    if login == 2707 and senha == 1995:
        print(" Seja bem vindo!")
        break

    numero_de_tentativa -= 1

    if numero_de_tentativa == 0:
        print("Acesso bloqueado")
    else:
        print(f"Tente novamente, restam {numero_de_tentativa} tentativas")
        


        
    