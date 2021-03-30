"""
Fúlvio Taroni Monteforte
Aluno de engenharia de computação do CEFET-MG.
"""

"""
Uma empresa contrata um encanador a R$70,00 por dia. Faça um programa que solicite o número de dias
trabalhado pelo encanador e imprima o valor sabendo que 8% é descontado para o imposto de renda 
"""

d = int(input("Informe o número de dias trabalhados: "))
s = d*70 - (d*70*8/100)
print(f'O salário líquido é: R${s:.2f}')
