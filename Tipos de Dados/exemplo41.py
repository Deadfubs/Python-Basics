"""
Fúlvio Taroni Monteforte
Aluno de engenharia de computação do CEFET-MG.
"""

"""
Exercícios retirados da geek university
Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas trabalhadas no mês.
Imprima o valor a ser pago ao funcionário, adicionando 10% sobre o valor calculado
"""

v = float(input("Informe o valor da hora de trabalho: "))
h = int(input("Informe o número de horas trabalhadas: "))

pagamento = (v * h) + ((v*h*10)/100)
print(f'Valor a ser pago ao funcionário é: R$ {pagamento:.2f}')