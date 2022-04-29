"""
Fúlvio Taroni Monteforte
Aluno de engenharia de computação do CEFET-MG.
"""

"""
Leia um valor em segundos e imprima no formato h:min:sec
"""

segundos = int(input("Informe o valor em segundos: "))
horas = segundos // 60 // 60
segundos %= 60*60
minutos = segundos // 60
segundos %= 60
print(f'O valor em datetime é: {horas:02}:{minutos:02}:{segundos:02}')
