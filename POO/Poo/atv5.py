class Fatura:
    def __init__(self, nomeItem, precoItem, qtdItem):
        self.nomeItem = nomeItem
        self.precoItrm = precoItem
        self.qtdItem = qtdItem
        self.total = 0

    def gerarFatura(self, total):
        self.total = total
        self.total = self.precoItem * self.qtdItem
        return f'O produto:{self.nome}'


produto1 = Fatura('Iphone', 7000, 2)
print(produto1.gerarFatura())

    