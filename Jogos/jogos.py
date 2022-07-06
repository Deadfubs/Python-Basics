import random
import adivinhacao
import forca


def escolhe_jogo():
    print("*********************************")
    print("*********Escolha o jogo**********")
    print("*********************************", end="\n\n")

    print("(1) Forca (2) Adivinhação")

    jogo = input("Qual jogo?\n")

    while not jogo.isnumeric():
        jogo = input("Não se finja de besta -_- digite um número: ")

    jogo = int(jogo)

    if jogo == 1:
        forca.jogar()
    elif jogo == 2:
        adivinhacao.jogar()
    else:
        print("Seu jogo será escolhido aleatoriamente...")
        jogo = random.randint(1, 2)
        if jogo == 1:
            forca.jogar()
        else:
            adivinhacao.jogar()


if __name__ == "__main__":
    escolhe_jogo()
