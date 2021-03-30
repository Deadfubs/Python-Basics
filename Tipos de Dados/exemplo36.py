"""
Fúlvio Taroni Monteforte
Aluno de engenharia de computação do CEFET-MG.
"""

"""
Leia a altura e o raio de um cilindro circular e informe seu volume
"""
pi = 3.141592
r = float(input("Informe o raio do cilindro: "))
h = float(input("Informe a altura do cilindro: "))

v = (pi * r**2)*h
print(f'Volume= {v:.6f}')
