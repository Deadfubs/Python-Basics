class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f"[>> Codigo: {self._codigo} | Saldo: {self._saldo} <<]"

    def __eq__(self, other):
        return self._codigo == other._codigo and self._saldo == other._saldo


conta1 = ContaSalario(37)
conta2 = ContaSalario(37)

print(conta1 == conta2)

contas = [conta1]

print(conta2 in contas)
