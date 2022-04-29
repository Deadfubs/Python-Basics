"""
Fúlvio Taroni Monteforte
Aluno de engenharia de computação do CEFET-MG.
"""

"""
Receba a altura do degrau de uma escada e a altura que o usuário deseja subir. Calcule quantos degraus o usuário preci-
sará subir.
"""

hd = float(input("Informe a altura do degrau da escada: "))
h = float(input("Informe a altura que deseja subir: "))

d = h/hd

if d % int(d) != 0:
    d = int(d) + 1

print(f"O usuário precisará subir: {d} degraus.")
