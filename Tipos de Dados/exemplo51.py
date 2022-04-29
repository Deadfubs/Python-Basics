"""
Aluno de engenharia de computação do CEFET-MG.
"""

"""
Receba as cordenadas x e y no R² e calcule a distância do ponto à origem (0,0)
"""

x, y = input("Informe as coordenadas (x, y): ").split(" ")
x = int(x)
y = int(y)

d = (x**2 + y**2)**(1/2)
print(f"A distância da origem é: {d}")
