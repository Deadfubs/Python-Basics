meu_texto = "Uma boneca que ganhou vida por magia, Gwen empunha as mesmas ferramentas que um dia a criaram."
meu_texto = meu_texto.lower()

aparicoes = dict()

for palavra in meu_texto.split():
    ate_agora = aparicoes.get(palavra, 0)
    aparicoes[palavra] = ate_agora + 1
print(aparicoes)


from collections import defaultdict

aparicoes2 = defaultdict(int)
for palavra in meu_texto.split():
    ate_agora = aparicoes2[palavra]
    aparicoes2[palavra] = ate_agora + 1

print(aparicoes2)

aparicoes3 = defaultdict(int)
for palavra in meu_texto.split():
    aparicoes3[palavra] += 1

print(aparicoes3)

class Conta:
    def __init__(self):
        print('Criando uma conta')

contas = defaultdict(Conta)
print(contas[15])
print(contas[15])

from collections import Counter

aparicoes4 = Counter(meu_texto.split())
print(aparicoes4)
