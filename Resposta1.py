# Crie uma Classe Bola

class Bola:

# Atributos: Cor, Circunferência, Material

    def __init__(self,Cor,Circunferência,Material):
        self.cor = Cor
        self.Circunferência = Circunferência
        self.Material = Material

# Metodós: TrocaCor e MostrarCor

    def TrocaCor(self,TC):
        self.cor = TC

    def MostrarCor(self):
        print(self.cor)

b = Bola('Verde',2,'Plastico')

b.MostrarCor()

b.TrocaCor('Azul')

b.MostrarCor()