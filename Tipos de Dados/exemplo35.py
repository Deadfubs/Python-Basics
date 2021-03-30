"""
Fúlvio Taroni Monteforte
Aluno de engenharia de computação do CEFET-MG.
"""

"""
Leia os catetos de um triângulo e calcule o valor da hipotenusa 
"""

print("Informe os catetos:")
a = float(input())
b = float(input())

h = (a**2 + b**2)**(1/2)
print(f'Hipotenusa: {h}')
