"""
Aluno de engenharia de computação do CEFET-MG.
"""

"""
Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor que cada um
deu para a aposta. Faça um programa que leia quanto cada um investiu e imprima a divisão de do prêmio para cada amigo.
"""

a, b, c = input("Informe quanto cada um investiu: ").split(" ")
p = float(input("Informe o valor do prêmio: "))

a = float(a)
b = float(b)
c = float(c)

total = a + b + c

p1 = p*(a/total)
p2 = p*(b/total)
p3 = p*(c/total)

print(f'A premiação do amigo 1 é: R$ {p1:.2f}')
print(f'A premiação do amigo 2 é: R$ {p2:.2f}')
print(f'A premiação do amigo 3 é: R$ {p3:.2f}')
