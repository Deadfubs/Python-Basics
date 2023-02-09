aparicoes = {'Gwen': 1, 'Sett': 3, 'Jax': 2, 'Camille': 6}
aparicoes2 = dict[('Gwen', 1), ('Sett', 3), ('Jax', 2), ('Camille', 6)]
aparicoes3 = dict(Gwen=1, Sett=3, Jax=2, Camille=6)

print(aparicoes3['Gwen'])

del aparicoes['Jax']
print(aparicoes)

print('Camille' in aparicoes)

for elemento in aparicoes3:
    print(elemento, aparicoes3[elemento])

for elemento in aparicoes3.keys():
    print(elemento)

for elemento in aparicoes3.values():
    print(elemento)

print(3 in aparicoes3.values())
print(aparicoes3.get('Camille'))

for elemento in aparicoes3.items():
    print(elemento)

for chave, valor in aparicoes3.items():
    print(chave, valor)

for chave, _ in aparicoes3.items():
    print(chave)

campeoes = [f'LoL {chave}' for chave in aparicoes3.keys()]
print(campeoes)

for i in sorted(aparicoes, key=aparicoes3.get, reverse=True):
    print(i, aparicoes[i])
