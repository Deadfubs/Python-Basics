import random as rand


def jogar():
    print("*********************************")
    print("Bem vindos ao jogo de adivinhação!")
    print("*********************************", end="\n\n")

    numero_secreto = rand.randint(0, 100)
    pontos = 1000
    print("(1) fácil (2) médio (3) difícil")
    dificuldade = input("Qual o nível de dificuldade?\n")

    while not dificuldade.isnumeric():
        dificuldade = input("Não se finja de besta -_- digite um número: ")

    dificuldade = int(dificuldade)

    while True:
        if dificuldade == 1:
            total_tentativas = 20
            break
        if dificuldade == 2:
            total_tentativas = 10
            break
        if dificuldade == 3:
            total_tentativas = 5
            break
        else:
            dificuldade = input("Valor inválido! Por favor, digite 1, 2 ou 3: ")
            while not dificuldade.isnumeric():
                dificuldade = input("Não se finja de besta -_- digite um número: ")
            dificuldade = int(dificuldade)

    for rodada in range(1, total_tentativas+1):
        print(f"Tentativa {rodada} de {total_tentativas}")
        chute = input("Digite um número entre 0 e 100: ")
        chute = int(chute)
        print(f"Seu chute foi: {chute}", end="\n\n")

        if chute < 0 or chute > 100:
            print('Você digitou um número inválido...')
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Você acertou, o universo foi salvo!")
            break
        elif rodada == total_tentativas:
            print("Todo o universo desapareceu!")
        else:
            if maior:
                print("Oh não, você errou e agora todo universo irá desaparecer! Ao menos que você "
                      "tente um valor menor...")
            elif menor:
                print("Oh não, você errou e agora todo universo irá desaparecer! Ao menos que você "
                      "tente um valor maior...")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos

    print(f"Sua pontuação foi: {pontos}")
    print("Fim de jogo!")


if __name__ == "__main__":
    jogar()
