import random


def mensagem_de_abertura():
    print("*********************************")
    print("Bem vindos ao jogo de forca!")
    print("*********************************", end="\n\n")


def preparar_palavra_secreta():
    palavras = list()
    with open("palavras_forca.txt") as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())

    index_palavra_secreta = random.randrange(0, len(palavras))

    palavra_secreta = palavras[index_palavra_secreta].upper()
    return palavra_secreta


def fim_de_jogo(executado, palavra_secreta):
    if executado:
        print("Puxa, você foi enforcado!")
        print(f"A palavra era {palavra_secreta}")
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")

    else:
        print("\n***********************************************")
        print(f"A palavra é: {palavra_secreta}")
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
    print("Fim de jogo!")


def confere_chute(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = chute.upper()
        index += 1


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def jogar():

    mensagem_de_abertura()

    palavra_secreta = preparar_palavra_secreta()
    executado = False
    livre = False
    letras_acertadas = ['_' for _ in palavra_secreta]
    letras_erradas = list()
    erros = 0
    total_tentativas = 7

    while not executado and not livre:
        print(f"Palavra: {letras_acertadas}")
        print(f"Letras erradas: {letras_erradas}")
        desenha_forca(erros)
        chute = input("Tente uma letra: ")
        chute = chute.strip().upper()

        if not(chute in palavra_secreta):
            letras_erradas.append(chute)
            erros += 1
        else:
            confere_chute(palavra_secreta, chute, letras_acertadas)

        palavra_formada = ''.join(letras_acertadas)
        if palavra_formada == palavra_secreta:
            livre = True
        executado = erros == total_tentativas

    fim_de_jogo(executado, palavra_secreta)


if __name__ == "__main__":
    jogar()
