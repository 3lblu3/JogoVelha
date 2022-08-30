def ganhador_3x3(linha1, linha2, linha3, nome1, nome2):
    """
    (linha1, linha2, linha3, nome1, nome2) \n
    (array, array, array, str, str) \n
    Retorna se há um vencedor ou não. \n
    Caso haja, ela te diz quem é.
    """
    ganhador1 = False  # contador para o placar
    ganhador2 = False  # contador para o placar
    # horizontal -> jogador1
    if (linha1[0] == 0) and (linha1[1] == 0) and (linha1[2] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True
    elif (linha2[0] == 0) and (linha2[1] == 0) and (linha2[2] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True
    elif (linha3[0] == 0) and (linha3[1] == 0) and (linha3[2] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True

    # vertical -> jogador1
    elif (linha1[0] == 0) and (linha2[0] == 0) and (linha3[0] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True
    elif (linha1[1] == 0) and (linha2[1] == 0) and (linha3[1] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True
    elif (linha1[2] == 0) and (linha2[2] == 0) and (linha3[2] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True

    # diagonais -> jogador1
    elif (linha1[0] == 0) and (linha2[1] == 0) and (linha3[2] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True
    elif (linha1[2] == 0) and (linha2[1] == 0) and (linha3[0] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True

    # o
    # horizontal -> jogador2
    elif (linha1[0] == 1) and (linha1[1] == 1) and (linha1[2] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True
    elif (linha2[0] == 1) and (linha2[1] == 1) and (linha2[2] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True
    elif (linha3[0] == 1) and (linha3[1] == 1) and (linha3[2] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True

    # vertical -> jogador2
    elif (linha1[0] == 1) and (linha2[0] == 1) and (linha3[0] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True
    elif (linha1[1] == 1) and (linha2[1] == 1) and (linha3[1] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True
    elif (linha1[2] == 1) and (linha3[2] == 1) and (linha3[2] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True

    # diagonais -> jogador2
    elif (linha1[0] == 1) and (linha2[1] == 1) and (linha3[2] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True
    elif (linha1[2] == 1) and (linha2[1] == 1) and (linha3[0] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True

    contador_velha = 0
    # ele me dirá se todos os espaços foi preenchido
    # se foi, então contador_velha == 0

    # velha
    for i in range(1):
        for j in linha1:
            if (j != 0) and (j != 1):
                contador_velha += 1
        for j in linha2:
            if (j != 0) and (j != 1):
                contador_velha += 1
        for j in linha3:
            if (j != 0) and (j != 1):
                contador_velha += 1

        if contador_velha == 0:
            print('O jogo deu velha!!')
    return ganhador1, ganhador2


def ganhador_4x4(linha1, linha2, linha3, linha4, nome1, nome2):
    """
    (linha1, linha2, linha3, linha4, nome1, nome2) \n
    (array, array, array, array, str, str) \n
    Retorna se há um vencedor ou não. \n
    Caso haja, ela te diz quem é.
    """
    ganhador1 = False  # contador para o placar
    ganhador2 = False  # contador para o placar
    # horizontal -> jogador1
    if (linha1[0] == 0) and (linha1[1] == 0) and (linha1[2] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True
    elif (linha1[1] == 0) and (linha1[2] == 0) and (linha1[3] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True

    elif (linha2[0] == 0) and (linha2[1] == 0) and (linha2[2] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True
    elif (linha2[1] == 0) and (linha2[2] == 0) and (linha2[3] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True

    elif (linha3[0] == 0) and (linha3[1] == 0) and (linha3[2] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True
    elif (linha3[1] == 0) and (linha3[2] == 0) and (linha3[3] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True

    elif (linha4[0] == 0) and (linha4[1] == 0) and (linha4[2] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True
    elif (linha4[1] == 0) and (linha4[2] == 0) and (linha4[3] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True

    # vertical -> jogador1
    elif (linha1[0] == 0) and (linha2[0] == 0) and (linha3[0] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True
    elif (linha2[0] == 0) and (linha3[0] == 0) and (linha4[0] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True

    elif (linha1[1] == 0) and (linha2[1] == 0) and (linha3[1] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True
    elif (linha2[1] == 0) and (linha3[1] == 0) and (linha4[1] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True

    elif (linha1[2] == 0) and (linha2[2] == 0) and (linha3[2] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True
    elif (linha2[2] == 0) and (linha3[2] == 0) and (linha4[2] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True

    elif (linha1[3] == 0) and (linha2[3] == 0) and (linha3[3] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True
    elif (linha2[3] == 0) and (linha3[3] == 0) and (linha4[3] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True

    # diagonais -> jogador1
    elif (linha1[0] == 0) and (linha2[1] == 0) and (linha3[2] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True
    elif (linha2[1] == 0) and (linha3[2] == 0) and (linha4[3] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True

    elif (linha1[3] == 0) and (linha2[2] == 0) and (linha3[1] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True
    elif (linha2[2] == 0) and (linha3[1] == 0) and (linha4[0] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True

    # o
    # horizontal -> jogador2
    elif (linha1[0] == 1) and (linha1[1] == 1) and (linha1[2] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True
    elif (linha1[1] == 1) and (linha1[2] == 1) and (linha1[3] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True

    elif (linha2[0] == 1) and (linha2[1] == 1) and (linha2[2] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True
    elif (linha2[1] == 1) and (linha2[2] == 1) and (linha2[3] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True

    elif (linha3[0] == 1) and (linha3[1] == 1) and (linha3[2] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True
    elif (linha3[1] == 1) and (linha3[2] == 1) and (linha3[3] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True

    elif (linha4[0] == 1) and (linha4[1] == 1) and (linha4[2] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True
    elif (linha4[1] == 1) and (linha4[2] == 1) and (linha4[3] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True

    # vertical -> jogador2
    elif (linha1[0] == 1) and (linha2[0] == 1) and (linha3[0] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True
    elif (linha1[1] == 1) and (linha2[1] == 1) and (linha3[1] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True
    elif (linha1[2] == 1) and (linha3[2] == 1) and (linha3[2] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True

    # diagonais -> jogador2
    elif (linha1[0] == 1) and (linha2[1] == 1) and (linha3[2] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True
    elif (linha2[1] == 1) and (linha3[2] == 1) and (linha4[3] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True

    elif (linha1[3] == 1) and (linha2[2] == 1) and (linha3[1] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True
    elif (linha2[2] == 1) and (linha3[1] == 1) and (linha4[0] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True

    contador_velha = 0
    # ele me dirá se todos os espaços foi preenchido
    # se foi, então contador_velha == 0

    # velha
    for i in range(1):
        for j in linha1:
            if (j != 0) and (j != 1):
                contador_velha += 1
        for j in linha2:
            if (j != 0) and (j != 1):
                contador_velha += 1
        for j in linha3:
            if (j != 0) and (j != 1):
                contador_velha += 1
        for j in linha4:
            if (j != 0) and (j != 1):
                contador_velha += 1

        if contador_velha == 0:
            print('O jogo deu velha!!')
    return ganhador1, ganhador2


def ganhador_5x5(linha1, linha2, linha3, linha4, linha5, nome1, nome2):
    """
    (linha1, linha2, linha3, linha4,linha5, nome1, nome2) \n
    (array, array, array, array, array, str, str) \n
    Retorna se há um vencedor ou não. \n
    Caso haja, ela te diz quem é.
    """
    ganhador1 = False  # contador para o placar
    ganhador2 = False  # contador para o placar
    # horizontal -> jogador1
    if (linha1[0] == 0) and (linha1[1] == 0) and (linha1[2] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True
    elif (linha1[1] == 0) and (linha1[2] == 0) and (linha1[3] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True
    elif (linha1[2] == 0) and (linha1[3] == 0) and (linha1[4] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True

    elif (linha2[0] == 0) and (linha2[1] == 0) and (linha2[2] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True
    elif (linha2[1] == 0) and (linha2[2] == 0) and (linha2[3] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True
    elif (linha2[2] == 0) and (linha2[3] == 0) and (linha2[4] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True

    elif (linha3[0] == 0) and (linha3[1] == 0) and (linha3[2] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True
    elif (linha3[1] == 0) and (linha3[2] == 0) and (linha3[3] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True
    elif (linha3[2] == 0) and (linha3[3] == 0) and (linha3[4] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True

    elif (linha4[0] == 0) and (linha4[1] == 0) and (linha4[2] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True
    elif (linha4[1] == 0) and (linha4[2] == 0) and (linha4[3] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True
    elif (linha4[2] == 0) and (linha4[3] == 0) and (linha4[4] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True

    elif (linha5[0] == 0) and (linha5[1] == 0) and (linha5[2] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True
    elif (linha5[1] == 0) and (linha5[2] == 0) and (linha5[3] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True
    elif (linha5[2] == 0) and (linha5[3] == 0) and (linha5[4] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True

    # vertical -> jogador1
    elif (linha1[0] == 0) and (linha2[0] == 0) and (linha3[0] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True
    elif (linha2[0] == 0) and (linha3[0] == 0) and (linha4[0] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True
    elif (linha3[0] == 0) and (linha4[0] == 0) and (linha5[0] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True

    elif (linha1[1] == 0) and (linha2[1] == 0) and (linha3[1] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True
    elif (linha2[1] == 0) and (linha3[1] == 0) and (linha4[1] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True
    elif (linha3[1] == 0) and (linha4[1] == 0) and (linha5[1] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True

    elif (linha1[2] == 0) and (linha2[2] == 0) and (linha3[2] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True
    elif (linha2[2] == 0) and (linha3[2] == 0) and (linha4[2] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True
    elif (linha3[2] == 0) and (linha4[2] == 0) and (linha5[2] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True

    elif (linha1[3] == 0) and (linha2[3] == 0) and (linha3[3] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True
    elif (linha2[3] == 0) and (linha3[3] == 0) and (linha4[3] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True
    elif (linha3[3] == 0) and (linha4[3] == 0) and (linha5[3] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True

    elif (linha1[4] == 0) and (linha2[4] == 0) and (linha3[4] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True
    elif (linha2[4] == 0) and (linha3[4] == 0) and (linha4[4] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True
    elif (linha3[4] == 0) and (linha4[4] == 0) and (linha5[4] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True

    # diagonais -> jogador1
    elif (linha1[0] == 0) and (linha2[1] == 0) and (linha3[2] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True
    elif (linha2[1] == 0) and (linha3[2] == 0) and (linha4[3] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True
    elif (linha3[2] == 0) and (linha4[3] == 0) and (linha5[4] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True

    elif (linha1[4] == 0) and (linha2[3] == 0) and (linha3[2] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True
    elif (linha2[3] == 0) and (linha3[2] == 0) and (linha4[1] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True
    elif (linha3[2] == 0) and (linha4[1] == 0) and (linha5[0] == 0):
        print(nome1 + ', você ganhou essa partida!!')
        ganhador1 = True

    # o
    # horizontal -> jogador2
    elif (linha1[0] == 1) and (linha1[1] == 1) and (linha1[2] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True
    elif (linha1[1] == 1) and (linha1[2] == 1) and (linha1[3] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True
    elif (linha1[2] == 1) and (linha1[3] == 1) and (linha1[4] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True

    elif (linha2[0] == 1) and (linha2[1] == 1) and (linha2[2] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True
    elif (linha2[1] == 1) and (linha2[2] == 1) and (linha2[3] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True
    elif (linha2[2] == 1) and (linha2[3] == 1) and (linha2[4] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True

    elif (linha3[0] == 1) and (linha3[1] == 1) and (linha3[2] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True
    elif (linha3[1] == 1) and (linha3[2] == 1) and (linha3[3] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True
    elif (linha3[2] == 1) and (linha3[3] == 1) and (linha3[4] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True

    elif (linha4[0] == 1) and (linha4[1] == 1) and (linha4[2] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True
    elif (linha4[1] == 1) and (linha4[2] == 1) and (linha4[3] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True
    elif (linha4[2] == 1) and (linha4[3] == 1) and (linha4[4] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True

    elif (linha5[0] == 1) and (linha5[1] == 1) and (linha5[2] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True
    elif (linha5[1] == 1) and (linha5[2] == 1) and (linha5[3] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True
    elif (linha5[2] == 1) and (linha5[3] == 1) and (linha5[4] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True

    # vertical -> jogador2
    elif (linha1[0] == 1) and (linha2[0] == 1) and (linha3[0] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True
    elif (linha2[0] == 1) and (linha3[0] == 1) and (linha4[0] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True
    elif (linha3[0] == 1) and (linha4[0] == 1) and (linha5[0] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True

    elif (linha1[1] == 1) and (linha2[1] == 1) and (linha3[1] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True
    elif (linha2[1] == 1) and (linha3[1] == 1) and (linha4[1] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True
    elif (linha3[1] == 1) and (linha4[1] == 1) and (linha5[1] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True

    elif (linha1[2] == 1) and (linha2[2] == 1) and (linha3[2] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True
    elif (linha2[2] == 1) and (linha3[2] == 1) and (linha4[2] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True
    elif (linha3[2] == 1) and (linha4[2] == 1) and (linha5[2] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True

    elif (linha1[3] == 1) and (linha2[3] == 1) and (linha3[3] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True
    elif (linha2[3] == 1) and (linha3[3] == 1) and (linha4[3] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True
    elif (linha3[3] == 1) and (linha4[3] == 1) and (linha5[3] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True

    elif (linha1[4] == 1) and (linha2[4] == 1) and (linha3[4] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True
    elif (linha2[4] == 1) and (linha3[4] == 1) and (linha4[4] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True
    elif (linha3[4] == 1) and (linha4[4] == 1) and (linha5[4] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True

    # diagonais -> jogador2
    elif (linha1[0] == 1) and (linha2[1] == 1) and (linha3[2] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True
    elif (linha2[1] == 1) and (linha3[2] == 1) and (linha4[3] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True
    elif (linha3[2] == 1) and (linha4[3] == 1) and (linha5[4] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True

    elif (linha1[4] == 1) and (linha2[3] == 1) and (linha3[2] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True
    elif (linha2[3] == 1) and (linha3[2] == 1) and (linha4[1] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True
    elif (linha3[2] == 1) and (linha4[1] == 1) and (linha5[0] == 1):
        print(nome2 + ', você ganhou essa partida!!')
        ganhador2 = True

    contador_velha = 0
    # ele me dirá se todos os espaços foi preenchido
    # se foi, então contador_velha == 0

    # velha
    for i in range(1):
        for j in linha1:
            if (j != 0) and (j != 1):
                contador_velha += 1
        for j in linha2:
            if (j != 0) and (j != 1):
                contador_velha += 1
        for j in linha3:
            if (j != 0) and (j != 1):
                contador_velha += 1
        for j in linha4:
            if (j != 0) and (j != 1):
                contador_velha += 1

        if contador_velha == 0:
            print('O jogo deu velha!!')
    return ganhador1, ganhador2