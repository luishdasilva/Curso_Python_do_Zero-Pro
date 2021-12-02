# Crie classe que modele um quadrado:

class Quadrado:

# Atributos: Tamanho do lado

    def __init__(self, Tamanhodolado):
        self.tamanhodolado = Tamanhodolado

# Métodos: Mudar Valor do lado, Retornar Valor do lado e calcular área

    def MVL(self,tdl):
        self.tamanhodolado = tdl

    def RVL(self):
        print(self.tamanhodolado)

    def CA(self):
        return self.tamanhodolado * self.tamanhodolado

q = Quadrado(2)

q.RVL()

q.MVL(3)

print(q.CA())