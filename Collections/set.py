usuarios_data_science = [13, 15, 25, 40]
usuarios_machine_learning = [13, 26, 40, 55]

assistiram = usuarios_machine_learning.copy()

print(assistiram)

assistiram.extend(usuarios_data_science)
print(assistiram)

assistiram = set(assistiram)

print(assistiram)

for usuario in assistiram:
    print(usuario)

usuarios_machine_learning = set(usuarios_machine_learning)
usuarios_data_science = set(usuarios_data_science)

print()
print(usuarios_machine_learning | usuarios_data_science)
print(usuarios_machine_learning & usuarios_data_science)
print(usuarios_data_science - usuarios_machine_learning)
print(usuarios_data_science ^ usuarios_machine_learning)
print()

usuarios = {1, 5, 76, 34, 16, 77, 17}
len(usuarios)
usuarios.add(14)

print(usuarios)

usuarios = frozenset(usuarios)
print(usuarios)

meu_texto = "Uma boneca que ganhou vida por magia, Gwen empunha as mesmas ferramentas que um dia a criaram."
meu_texto = set(meu_texto.split())

print(meu_texto)
