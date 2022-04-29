"""
Fúlvio Taroni Monteforte
Aluno de engenharia de computação do CEFET-MG.
"""
"""
Programa para ajudar vendedores
"""
c=float(input("Informe o valor total das compras: "))

print(f'\nTotal a pagar com desconto: R$ {(c - c*10/100):.2f}')
print(f'Parcela (3x sem juros): R$ {(c/3):.2f}')
print(f'Comissão do vendedor a vista: R$ {((c - c*10/100)*5/100):.2f}')
print(f'Comissão do vendedor parcelado: R$ {(c*5/100):.2f}')