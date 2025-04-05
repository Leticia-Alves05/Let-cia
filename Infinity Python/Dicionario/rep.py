empresa = {
    "nome": "Infinity School",
    "endereço": "Av.Contorno",
    "Quantidade Alunos": 300
}

empresa["Quantidade Alunos"] = 500
print(empresa)






compras = {           
    "supermercado": ["leite", "feijão","arroz","ovo"],
    "açougue":"carne",
    "sacolão":"tomate"
}

# compras["padaria"] = "pão"
compras.update({"padaria": "pão"})
print(compras)



print(compras.get("loja", "Esse item não existe no dicionario."))






























tarefas = {
    "Nome da Tarefa": None,
    "Descrição da tarefa": None,
    "Status": True,
    "Prioridade": None
}



tarefas["Status"] = False




















lista = []

nome = input("Digite seu nome")
lista.append(nome)