"""
Fúlvio Taroni Monteforte
Aluno de engenharia de computação do CEFET-MG.
"""

"""
Exercícios retirados da geek university
Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo-se que esse funcionário tem uma
gratificação de 5% sobre o salário base. Além disso ele paga 7% de imposto sobre o salário-base.
"""

sb = float(input("Informe o salário-base do funcionário: "))

sr = sb + (sb * 5/100) - (sb * 7/100)

print(f"O salário a receber do funcionário é: {sr:.2f}")
