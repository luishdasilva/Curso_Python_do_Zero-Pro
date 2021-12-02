# Crie um Programa que tenha uma classe carro

class Carro:

# Este programa deve ter no minimo 3 propriedades para a classe carro

    def __init__(self,Porta,Motor,Volante):
        self.porta = Porta
        self.volante = Volante
        self.motor = Motor

# E no minimo 3 métodos para ela, sendo um destes métodos para imprimir todos os dados do carro

    def abre(self):
        return print(self.porta, 'Abertas')

    def fecha(self):
        return print(self.porta, 'Fechadas')

    def visão(self):
        return print('Quantidade de portas',self.porta,'Volante',self.volante,'Motor',self.motor)

#celta = Carro(4,1,1)
#celta.abre()
#celta.fecha()
#celta.visão()
#Ferrari = Carro(2,1,1)
#Ferrari.abre()
#Ferrari.fecha()
#Ferrari.visão()
#Corsa = Carro(2,1,1)
#Corsa.abre()
#Corsa.fecha()
#Corsa.visão()