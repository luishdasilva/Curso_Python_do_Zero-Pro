# Faça um programa que simule um televisor criando o como um objeto

class TV:

    def __init__(self,Canal,Volume):
        self.canal = Canal
        self.volume = Volume

# O usuário deve ser capaz de informar o numero do canal

class Programa(TV):

    def __init__(self):
        pass

    def entrada(self):
        while True:
            informe = int(input('Informe o numero do Canal: '))
            if informe <= 50:
                self.canal = informe
                print('Agora o canal é: {} '.format(self.canal))
            else:
                print('Informe o canal com numeros inteiros e de 1 até 50')
                return informe
            break

        while True:
            per = str(input('Deseja Aumentar ou Diminuir o Volume: (S/N)'))
            if per == 'S':
                aum = int(input('Digite o volume que deseja aumentar de 1 até 50: '))
                if aum <= 50:
                    self.volume = aum
                    print('O Volume foi aumentado para: {}'.format(self.volume))
                else:
                    print('Informe o volume com numeros inteiros e de 1 até 50')
                    break
            else:
                break




p = Programa()


p.entrada()