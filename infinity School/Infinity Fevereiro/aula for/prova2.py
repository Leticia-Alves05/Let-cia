
numero_de_tentativa = 2

while numero_de_tentativa != 0:
    login = (input('Digite o login: '))
    senha = int(input("Digite sua senha: "))
    if login == 578 and senha == 1234:
        print(" Seja bem vindo!")
        break
    if login != 578 or senha != 1234:
        print(f" restam {numero_de_tentativa} tentativas")
        numero_de_tentativa -= 1


" Crie um programa em Python que simule um sistema de login. O programa deve permitir ao usuário três tentativas para acertar o nome de usuário e a senha corretos. Caso o usuário erre as credenciais, o programa deve fornecer uma mensagem informando quantas tentativas restam. Se o usuário acertar, uma mensagem de boas-vindas deve ser exibida, e o programa deve terminar imediatamente.Se todas as três tentativas falharem, o programa deve usar um loop for para exibir uma mensagem de Acesso bloqueado repetida três vezes."