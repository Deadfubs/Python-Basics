"""
Fúlvio Taroni Monteforte
Aluno de engenharia de computação do CEFET-MG.
"""

"""
O valor de 780.000,00 BRL será dividido entre três ganhadores de um concurso
- O 1º receberá 46%
- O 2º receberá 32%
- O 3º receberá o restante
"""

a = 780_000 * 46/100
b = 780_000 * 32/100
c = 780_000 - a - b

print(f'1º: R$ {a:.2f}')
print(f'2º: R$ {b:.2f}')
print(f'3º: R$ {c:.2f}')
