"""
Fúlvio Taroni Monteforte
Aluno de engenharia de computação do CEFET-MG.
"""

"""
Converter maiúsculo em minúsculo usando a tabela ASCII
"""

"""
ord() retorna um inteiro representando o caractére Unicode
chr() retorna um  caractére Unicode  a partir do inteiro
"""
ch = str(input("Informe a letra maiúscula: "))

print(f"A letra minúscula é: {chr(ord(ch)+32)}")
