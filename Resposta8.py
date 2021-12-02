#classe Bomba de Combustivel

class BombadeCombustivel:

# Atributos: tipoCombustivel, valorLitro, quantidadeCombustivel

    def __init__(self,tipoCombustivel,valorLitro,quantidadeCombustivel):
        self.tipocombustivel = tipoCombustivel
        self.valorlitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

# Métodos: AbastecerPorvalor , AbastecerPorLitro, Alterarvalor, alterarCombustivel, alterarquantidadeCombustivel

    def abastecerporvalor(self,real):
        self.real = real
        litro = self.real / self.valorlitro
        bomba = self.quantidadeCombustivel - litro
        print('foi abastecido:',self.real,'R$ e foi colocado: ',litro,'litros',bomba,'litros na Bomba')

    def abastecerporlitro(self,litro):
        self.litro = litro
        pago = self.valorlitro * self.litro
        bomba = self.quantidadeCombustivel - self.litro
        print('foi abastecido:',self.litro,'litros e deve ser pago: ',pago,'R$',bomba,'litros na Bomba')


    def alterarvalor(self,alterarvalorlitro):
        self.valorlitro = alterarvalorlitro

    def alterarcombustivel(self,valorcombustivel):
        self.tipocombustivel = valorcombustivel

    def alterarquantidadecombustivel(self,quantcombustivel):
        self.quantidadeCombustivel = quantcombustivel

c = BombadeCombustivel('Comum',5,10000)

c.abastecerporvalor(10)
c.abastecerporlitro(2)
c.alterarvalor(10)
c.alterarcombustivel('Adtivada')
c.alterarquantidadecombustivel(9000)
c.abastecerporvalor(20)
c.abastecerporlitro(4)