
class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def sobrenome(self):
        return self.__sobrenome

    @property
    def cpf(self):
        return self.__cpf


class Conta:
    def __init__(self, numero, titular, saldo, limite=100):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    def saca(self, valor):
        if valor > self.__saldo or valor <= 0:
            print("Valor de saque inválido")
        else:
            self.__saldo -= valor
            return True

    def deposita(self, valor):
        self.__saldo += valor
        return True

    def extrato(self):
        print(f"Conta: {self.__numero}\nSaldo: {self.__saldo}")

    def transfere_para(self, destino, valor):
        sucesso = self.saca(valor)
        if not sucesso:
            print("Transferência sem sucesso!")
        else:
            destino.__saldo += valor
            return True

if __name__ == '__main__':
    print('Importe esse programa')
