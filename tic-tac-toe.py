#!/usr/bin/env python

quadro = [" " for i in range(9)]


def mostrar_quadro():
    linha1 = "|{}|{}|{}|".format(quadro[0], quadro[1], quadro[2])
    linha2 = "|{}|{}|{}|".format(quadro[3], quadro[4], quadro[5])
    linha3 = "|{}|{}|{}|".format(quadro[6], quadro[7], quadro[8])

    print()
    print(linha1)
    print(linha2)
    print(linha3)
    print()


def validar_escolha(escolha):
    try:
        escolha = int(escolha)
    except ValueError:
        return False

    if escolha not in list(range(1, 9)):
        return False

    return True


def ler_escolha():
    while True:
        escolha = input(
            "Digite um numero para marcar o quadro (1-9): "
        ).strip()

        if validar_escolha(escolha):
            return int(escolha)

        print("Valor inválido! Tente novamente.")


def movimento_jogador(icone):
    if icone == "X":
        num = 1
    elif icone == "O":
        num = 2

    print("A vez do jogador {}.".format(num))

    escolha = ler_escolha()

    if quadro[escolha - 1] == " ":
        quadro[escolha - 1] = icone
    else:
        print()
        print("Esse ja foi marcado!")
        mostrar_quadro()
        movimento_jogador(icone)


def vitoria(icone):
    if (quadro[0] == icone and quadro[1] == icone and quadro[2] == icone) or \
        (quadro[3] == icone and quadro[4] == icone and quadro[5] == icone) or \
        (quadro[6] == icone and quadro[7] == icone and quadro[8] == icone) or \
        (quadro[0] == icone and quadro[3] == icone and quadro[6] == icone) or \
        (quadro[1] == icone and quadro[4] == icone and quadro[7] == icone) or \
        (quadro[2] == icone and quadro[5] == icone and quadro[8] == icone) or \
        (quadro[0] == icone and quadro[4] == icone and quadro[8]) == icone or \
            (quadro[2] == icone and quadro[4] == icone and quadro[6] == icone):
        return True
    else:
        return False


def empate():
    if " " not in quadro:
        return True
    else:
        return False


def main():
    while True:
        mostrar_quadro()
        movimento_jogador("X")
        mostrar_quadro()
        if vitoria("X"):
            print("X venceu! Parabens!")
            break
        elif empate():
            print("Jogo EMPATADO!")
            break
        movimento_jogador("O")
        if vitoria("O"):
            print("O venceu! Parabens!")
            break
        elif empate():
            print("Jogo EMPATADO!")
            break


main()
