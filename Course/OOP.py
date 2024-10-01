
# Abstraçao e encapsulamento

class Conta:
    contador = 400

    def __init__(self, titular, saldo, limite):
        self.numero = Conta.contador
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

        Conta.contador += 1        

    def toString(self):
        print(self.__dict__)

conta1 = Conta('Fabian', 1700, 1000)
conta1.toString()
