"""
Fúlvio Taroni Monteforte
Aluno de engenharia de computação do CEFET-MG.
"""

"""
Exercícios retirados da geek university
Leia um valor em real e a cotação atual do dólar e imprima o valor correspondente em dólares
"""

r = float(input("Informe o valor em reais: "))
c = float(input("Informe a cotação do dólar: "))

d = r/c

print(f'O valor em dólares é: {d:.2f}USD')