# operações com listas--------------------------------------------------------------------------------------------------
idades = [20, 39, 18]
print(idades)

idades.append([27, 19])
print(idades)

idades.remove([27, 19])
print(idades)

idades.extend([27, 19])
print(idades)

idades.pop(4)
print(idades)

idades_no_ano_que_vem = [idade+1 for idade in idades]
print(idades_no_ano_que_vem)

idades_maiores_que_21 = [idade for idade in idades if idade > 21]
print(idades_maiores_que_21)
# ----------------------------------------------------------------------------------------------------------------------

# mutabilidade das listas-----------------------------------------------------------------------------------------------
print("\nMutabilidade das listas:")


def faz_processamento_da_lista(lista=None):
    if lista is None:
        lista = list()
    print(len(lista))
    lista.append(13)


idades2 = [16, 21, 29, 56, 43]
faz_processamento_da_lista(idades2)
print(idades2)

faz_processamento_da_lista()
faz_processamento_da_lista()
