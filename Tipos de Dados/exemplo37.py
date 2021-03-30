"""
Fúlvio Taroni Monteforte
Aluno de engenharia de computação do CEFET-MG.
"""

"""
Faça um programa que leia o valor de um produto e aplique um desconto de 12% nele
"""

r = float(input('Informe o valor do produto: '))

r = r - (r*12/100)
print(f"O valor com descnto é: {r:.2f} BRL")
