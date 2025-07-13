

class Carro: 
#metodo contrutor
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano 
        self.velocidade = 0
#metodo
    def __str__(self):
        return f'O {self.modelo} da marca {self.marca} é do ano: {self.ano}'
    
#metodo que printa o modelo do carro ligando
    def ligar(self):
        return f'O carro {self.modelo} esta ligado'
    
#metodo que aumenta a velocidade(self.velocidade) do carro e printa 
    def acelerar(self): 
        self.velocidade += 10
        print(f'{self.modelo} está a {self.velocidade}KM/H')
    
#metodo que abaixa a velocidade(self.velocidade) do carro e printa 
    def frear(self): 
        self.velocidade -= 5
        print(f'{self.modelo} está a {self.velocidade}KM/H')


#Criação dos objetos de acordo com a Classe
carro1 = Carro('Chevy', 'Corvette', 1975)
carro2 = Carro('Volks', 'Gol', 2003)

#utilizando os metodos da Classe no primeiro Objeto
carro1.acelerar() 
carro1.acelerar()
carro1.frear()

#utilizando os metodos da Classe no segundo objeto
carro2.acelerar() 
carro2.frear()

