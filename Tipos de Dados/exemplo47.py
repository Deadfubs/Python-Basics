"""
Fúlvio Taroni Monteforte
Aluno de engenharia de computação do CEFET-MG.
"""

"""
Imprimir os digitos de um número inteiro por linha
"""

n = int(input("Informe o número: "))
n = int(str(n)[::-1])

print("Os digitos em linhas são:")
while n != 0:
    print(f'{n%10}')
    n = int(n/10)
