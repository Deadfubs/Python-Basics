from operator import attrgetter
from functools import total_ordering

idades = [15, 87, 55, 34, 25, 13, 27, 42]
# enumerate
print(list(enumerate(idades)))

print()
for indice, valor in enumerate(idades):
    print(indice, valor)

print()
for indice, _ in enumerate(idades):
    print(indice)

# ordenação natural

print(sorted(idades))
print(list(reversed(idades)))  # reverso, não ordenado ao contrário
print(sorted(idades, reverse=True))
print(list(reversed(sorted(idades))))

print(idades.sort())
print(idades)


# ordenação customizada

@total_ordering
class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f"[>> Codigo: {self._codigo} | Saldo: {self._saldo}<<]"

    def __eq__(self, other):
        return self._codigo == other._codigo and self._saldo == other._saldo

    def __lt__(self, other):
        if self._saldo != other.saldo:
            return self._saldo < other.saldo
        return self._codigo < other._codigo

    @property
    def saldo(self):
        return self._saldo


conta1 = ContaSalario(15)
conta1.deposita(500)

conta2 = ContaSalario(17)
conta2.deposita(700)

conta3 = ContaSalario(20)
conta3.deposita(100)

conta4 = ContaSalario(255)
conta4.deposita(700)

contas = [conta1, conta2, conta3]


def extrai_saldo(conta):
    return conta.saldo

print()
for conta in sorted(contas, key=attrgetter("saldo")):
    print(conta)

print()
print(conta1 < conta2)

print()
for conta in sorted(contas):
    print(conta)

# ordenação total

contas2 = [conta1, conta2, conta3, conta4]

print()
for conta in sorted(contas2, key=attrgetter("saldo", "_codigo")):
    print(conta)

print()
for conta in sorted(contas2):
    print(conta)

print(conta2 < conta4)