"""
Aluno de engenharia de computação do CEFET-MG.
"""

"""
Leia o horário(hora, minuto, segundo) de início de uma experiência e a duração em segundos, imprima o horário do término
da experiência
"""

horas, minutos, segundos = input("Informe o horário do início da experiência (hh:mm:ss): ").split(":")
duracao = int(input("Informe a duração da experiência em segundos: "))

inicio = (int(horas)*60*60) + (int(minutos)*60) + (int(segundos))

termino = inicio + duracao

segundos = termino
horas = segundos // 60 // 60
segundos %= 60*60
minutos = segundos // 60
segundos %= 60
print(f'O horário de término da experiência foi: {horas:02}:{minutos:02}:{segundos:02}')
