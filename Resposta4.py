# Crie uma classe que modele uma pessoa

class Pessoa:

# Atributos: Nome, idade , peso e altura

    def __init__(self,nome,idade,peso,altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

# métodos: Envelhecer , engordar , emagrecer, crescer
# Obs: Por padrão, a cada ano que a pessoa envelhece, sendo a idade dela menor que  21 anos ela deve crescer 0,5 cm

    def Envelhecer(self,quantosanosenvelhercer):
        return self.idade + quantosanosenvelhercer

    def Engordar(self,kilos):
        return self.peso + kilos

    def Emagrecer(self,Perdeu):
        return self.peso - Perdeu

    def crescer(self):
        if self.idade <= 21:
          print(self.altura + 0.05)
        else:
            pass



p = Pessoa('Bruno',10,30,1.50)

p.crescer()
print(p.Envelhecer(3))

#print(p.Engordar(2))

#print(p.Emagrecer(2))

