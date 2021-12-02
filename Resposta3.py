# Crie uma Classe que modele um Retangulo

class Retangulo:

# Atributos: LadoA, LadoB

    def __init__(self,LadoA,LadoB):
        self.LadoA = LadoA
        self.LadoB = LadoB

# Métodos: Mudar Valor dos Lados, Retornar Valor dos Lados , Calcular área, Calcular Perimetro

    def MVL(self,LA,LB):
        self.LadoA = LA
        self.LadoB = LB

    def RVL(self):
        print(self.LadoA,self.LadoB)

    def CA(self):
        return self.LadoA * self.LadoB

    def CP(self):
        return 2 * (self.LadoA + self.LadoB)

#r = Retangulo(3,3)

#r.RVL()

#r.MVL(40,4)

#r.RVL()

#print(r.CA())

#print(r.CP())

# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe
# as medidas de um local. Depois deve criar um objeto com as medidas
class Programa(Retangulo):

    def __init__(self,Base,Largura):
        self.LadoA = Base
        self.LadoB = Largura

    def entrada(self):
        self.LadoA = int(input('Informe o valor da Base: '))
        self.LadoB = int(input('Informe o valor da Largura: '))



p = Programa(2,2)

p.entrada()

print('Quantidade de Pisos: ',p.CA(),'m²')
print('Quantidade de Rodapé: ',p.CP())