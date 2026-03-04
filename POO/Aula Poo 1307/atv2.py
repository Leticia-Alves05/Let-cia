class Funcionario:
    def __init__(self, nome: str, cpf: int, salario_bruto: float):
        self.nome = nome
        self.cpf = cpf
        self.salario_bruto = salario_bruto

    def calcular_salario_liquido(self):
        desconto = self.salario_bruto * 0.03 
        salario_liquido = self.salario_bruto - desconto
        return salario_liquido
    def __str__(self):
        salario_liquido = self.calcular_salario_liquido()
        return f'Nome: {self.nome}\nCPF: {self.cpf}\nSalario: {salario_liquido}'
    
f1 = Funcionario('João', 123456789, 5000)
print(f1)

class Gerente(Funcionario):
    def __init__(self, nome: str, cpf: int, salario_bruto: float, setor: str):
        super().__init__(nome, cpf, salario_bruto)
        self.setor = setor
    
    def calcular_salario_liquido(self):
        salario_liquido = self.salario_bruto -(self.salario_bruto * 0.07)
        return salario_liquido

gerente = Gerente('Ana', 987654321, 6000, 'Vendas')
print(gerente)
