class Conta:
    def __init__(self, numero, titular, saldo, limite=1000.0):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    # Propriedades------------------------------------------------------------------------------------------------------
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

    @limite.setter
    def limite(self, limite):
        self.__limite = limite
    # ------------------------------------------------------------------------------------------------------------------

    # Métodos estáticos-------------------------------------------------------------------------------------------------
    @ staticmethod
    def codigo_banco():
        return "001"

    @ staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
    # ------------------------------------------------------------------------------------------------------------------

    # Métodos privados--------------------------------------------------------------------------------------------------
    def __autoriza_saque(self, valor):
        valor_disponivel = self.__saldo + self.__limite
        return valor_disponivel >= valor
    # ------------------------------------------------------------------------------------------------------------------

    def extrato(self):
        print(f"Saldo do titular {self.__titular}: {self.__saldo}")

    def deposito(self, valor):
        self.__saldo += valor

    def saque(self, valor):
        if self.__autoriza_saque(valor):
            self.__saldo -= valor
        else:
            print("Limite insuficiente")

    def transferencia(self, valor, destino):
        self.saque(valor)
        destino.deposito(valor)
