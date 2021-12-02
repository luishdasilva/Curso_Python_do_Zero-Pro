# Classe conta corrente

class ContaCorrente:

# Atributos: Numero da conta , nome do correntista e saldo
    def __init__(self,Numerodaconta,Nome,Saldo = 0): # saldo é opcional
        self.conta = Numerodaconta
        self.nome = Nome
        self.saldo = Saldo

# métodos: alterarNome, depósito e saque
    def alterarNome(self,alterar):
        self.nome = alterar

    def deposito(self,depositar):
        self.saldo = self.saldo + depositar

    def saque(self,Saque):
        self.saldo = self.saldo - Saque


    def imprime(self):
        print(self.conta,self.nome,self.saldo)

c = ContaCorrente(10,'Bruno')

c.alterarNome('Fabio')
c.deposito(50)
c.saque(20)
c.imprime()