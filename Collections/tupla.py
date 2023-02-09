class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return f"[>> Codigo: {self.codigo} | Saldo: {self.saldo} <<]"


def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)


conta1 = ContaCorrente(15)
conta1.deposita(100)


conta2 = ContaCorrente(18)
conta2.deposita(1000)

contas = (conta1, conta2)
for conta in contas:
    print(conta)

deposita_para_todas(contas)
for conta in contas:
    print(conta)


# variação funcional com tuplas
conta_do_gui = (15, 1000)

def deposita(conta):
    novo_saldo = conta[1] + 100
    codigo = conta[0]
    return (codigo, novo_saldo)
print(deposita(conta_do_gui))
