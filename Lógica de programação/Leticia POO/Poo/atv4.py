class Calculadora:
    def __init__(self,valor1, valor2):
        self.valor1 = valor1           
        self.valor2 = valor2

    def soma(self):
        return self.valor1 + self.valor2
    
    def divisao(self):
        return self.valor1 / self.valor2
    




print(Calculadora(5, 5).soma())
print(Calculadora(5, 5).divisao())