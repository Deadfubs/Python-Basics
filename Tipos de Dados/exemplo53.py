"""
Aluno de engenharia de computação do CEFET-MG.
"""

"""
Leia a largura e comprimento de um terreno, bem como o valor do m² de tela e informee o custo para cercar todo esse
terreno com tela
"""

b, h = input("Informe as dimensões do terreno: ").split(" ")
b = float(b)
h = float(h)

m2 = float(input("Informe o custo do m² de tela: "))

custo = b * h * m2

print(f"O custo para telar todo o terreno é: R${custo:.2f}")
