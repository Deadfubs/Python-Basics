"""
Fúlvio Taroni Monteforte
Aluno de engenharia de computação do CEFET-MG.
"""

"""
Leia o salário de um funcionário e aplique um aumento de 25%
"""

r = float(input("Informe o salário do funcionário: "))
r = r + (r*25/100)
print(f'O novo salário é: {r:.2f} BRL')
