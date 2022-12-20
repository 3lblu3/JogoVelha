import funcoes_erro
import funcoes_ganhador

# 3x3 jogo
def jogada_3x3(nome1, nome2, n_partidas):
    """
    (nome_jogador1, nome_jogador2, qtnd de partidas) \n
    (str, str, int) \n
    Executa o jogo da velha!!
    """
    placar_x = 0
    placar_o = 0
    partida = 1
    while partida <= n_partidas:
        if partida != 1:
            print()
            print(f'Esta é a {partida}°, okay!!? \n')
        # declaração de variáveis para lá na frente substituir por 0 ou 1
        # jogador1 == 0
        # jogador2 == 1
        a_lista = [11, 12, 13]
        b_lista = [21, 22, 23]
        c_lista = [31, 32, 33]

        # rodada de 9 jogadas
        print(*a_lista, sep='|')
        print(*b_lista, sep='|')
        print(*c_lista, sep='|')
        print()

        n_jogada = 1
        while n_jogada <= 9:
            contador = n_jogada % 2
            # se contador != 0 -> jogada ímpar -> jogador1 -> 0
            # se contador == 0 -> jogada par -> jogador2 -> 1
            if contador != 0:
                jogando = input(f'{nome1}, digite sua jogada linhaXcoluna (11, 21, 23, ...): ')
                # irá passar o resultado e verificar erros
                jogando = funcoes_erro.erro_3x3(a_lista, b_lista, c_lista, jogando)
                n_linha = jogando[0]
                n_coluna = jogando[1]
                n_linha = int(n_linha)  
                n_coluna = int(n_coluna)  
                n_coluna = n_coluna - 1  # a contagem na lista começa do 0, por isso sub(1)
                if n_linha == 1:
                    a_lista[n_coluna] = 0
                elif n_linha == 2:
                    b_lista[n_coluna] = 0

                elif n_linha == 3:
                    c_lista[n_coluna] = 0

            else:
                jogando = input(f'{nome2}, digite sua jogada linhaXcoluna (11, 21, 23, ...): ')
                jogando = funcoes_erro.erro_3x3(a_lista, b_lista, c_lista, jogando)
                n_linha = jogando[0]
                n_coluna = jogando[1]
                n_linha = int(n_linha)  
                n_coluna = int(n_coluna)  
                n_coluna = n_coluna - 1  # a contagem na lista começa do 0, por isso sub(1)
                if n_linha == 1:
                    a_lista[n_coluna] = 1
                elif n_linha == 2:
                    b_lista[n_coluna] = 1

                elif n_linha == 3:
                    c_lista[n_coluna] = 1
            i = 1

            # print tabuleito
            while i < 4:
                # jogador1 == 0 == x
                # jogador2 == 1 == o
                if i == 1:
                    for j in a_lista:
                        if j == 0:
                            print(' x', end=' ')
                        elif j == 1:
                            print(' o', end=' ')
                        elif (j != 1) and (j != 0):
                            print(j, end=' ')
                    print()

                if i == 2:
                    for j in b_lista:
                        if j == 0:
                            print(' x', end=' ')
                        elif j == 1:
                            print(' o', end=' ')
                        elif (j != 1) and (j != 0):
                            print(j, end=' ')
                    print()

                if i == 3:
                    for j in c_lista:
                        if j == 0:
                            print(' x', end=' ')
                        elif j == 1:
                            print(' o', end=' ')
                        elif (j != 1) and (j != 0):
                            print(j, end=' ')
                    print()
                i += 1

            print()
            # saber se há ganhador
            win = funcoes_ganhador.ganhador_3x3(a_lista, b_lista, c_lista, nome1, nome2)
            if win[0]:
                placar_x = placar_x + 1
                break
            elif win[1]:
                placar_o = placar_o + 1
                break
            n_jogada += 1

        # verifica se há uma nova partida ou se está na última partida
        if partida < n_partidas:
            print('-' * 60)
            print('Uma nova partida já vai começar!!')
            print('-' * 60)
        partida += 1

    # mostra o placar quando há mais de uma partida
    if n_partidas != 1:
        print('-' * 60)
        print(f'Placar final das {n_partidas} partidas ({nome1} X {nome2}): {placar_x} X {placar_o}')
        print('-' * 60)


# 4x4 jogo
def jogada_4x4(nome1, nome2, n_partidas):
    """
    (nome_jogador1, nome_jogador2, qtnd de partidas) \n
    (str, str, int) \n
    Executa o jogo da velha!!
    """
    placar_x = 0
    placar_o = 0
    partida = 1
    while partida <= n_partidas:
        if partida != 1:
            print()
            print(f'Esta é a {partida}°, okay!!? \n')
        # declaração de variáveis para lá na frente substituir por 0 ou 1
        # jogador1 == 0
        # jogador2 == 1
        a_lista = [11, 12, 13, 14]
        b_lista = [21, 22, 23, 24]
        c_lista = [31, 32, 33, 34]
        d_lista = [41, 42, 43, 44]

        # rodada de 9 jogadas
        print(*a_lista, sep='|')
        print(*b_lista, sep='|')
        print(*c_lista, sep='|')
        print(*d_lista, sep='|')
        print()

        n_jogada = 1
        while n_jogada <= 9:
            contador = n_jogada % 2
            # se cantador != 0 -> jogada ímpar -> jogador1 -> 0
            # se cantador == 0 -> jogada par -> jogador2 -> 1
            if contador != 0:
                jogando = input(f'{nome1}, digite sua jogada linhaXcoluna (11, 21, 23, ...): ')
                # irá passar o resultado e verificar erros
                jogando = funcoes_erro.erro_4x4(a_lista, b_lista, c_lista, d_lista, jogando)
                n_linha = jogando[0]
                n_coluna = jogando[1]
                n_linha = int(n_linha)  
                n_coluna = int(n_coluna)  
                n_coluna = n_coluna - 1  # a contagem na lista começa do 0, por isso sub(1)
                if n_linha == 1:
                    a_lista[n_coluna] = 0
                elif n_linha == 2:
                    b_lista[n_coluna] = 0
                elif n_linha == 3:
                    c_lista[n_coluna] = 0
                elif n_linha == 4:
                    d_lista[n_coluna] = 0

            else:
                jogando = input(f'{nome2}, digite sua jogada linhaXcoluna (11, 21, 23, ...): ')
                jogando = funcoes_erro.erro_4x4(a_lista, b_lista, c_lista, d_lista, jogando)
                n_linha = jogando[0]
                n_coluna = jogando[1]
                n_linha = int(n_linha)  
                n_coluna = int(n_coluna)  
                n_coluna = n_coluna - 1  # a contagem na lista começa do 0, por isso sub(1)
                if n_linha == 1:
                    a_lista[n_coluna] = 1
                elif n_linha == 2:
                    b_lista[n_coluna] = 1
                elif n_linha == 3:
                    c_lista[n_coluna] = 1
                elif n_linha == 4:
                    d_lista[n_coluna] = 1
            i = 1

            # print tabuleito
            while i < 5:
                # jogador1 == 0 == x
                # jogador2 == 1 == o
                if i == 1:
                    for j in a_lista:
                        if j == 0:
                            print(' x', end=' ')
                        elif j == 1:
                            print(' o', end=' ')
                        elif (j != 1) and (j != 0):
                            print(j, end=' ')
                    print()

                if i == 2:
                    for j in b_lista:
                        if j == 0:
                            print(' x', end=' ')
                        elif j == 1:
                            print(' o', end=' ')
                        elif (j != 1) and (j != 0):
                            print(j, end=' ')
                    print()

                if i == 3:
                    for j in c_lista:
                        if j == 0:
                            print(' x', end=' ')
                        elif j == 1:
                            print(' o', end=' ')
                        elif (j != 1) and (j != 0):
                            print(j, end=' ')
                    print()
                if i == 4:
                    for j in d_lista:
                        if j == 0:
                            print(' x', end=' ')
                        elif j == 1:
                            print(' o', end=' ')
                        elif (j != 1) and (j != 0):
                            print(j, end=' ')
                    print()
                i += 1

            print()
            # saber se há ganhador
            win = funcoes_ganhador.ganhador_4x4(a_lista, b_lista, c_lista, d_lista, nome1, nome2)
            if win[0]:
                placar_x = placar_x + 1
                break
            elif win[1]:
                placar_o = placar_o + 1
                break
            n_jogada += 1

        # verifica se há uma nova partida ou se está na última partida
        if partida < n_partidas:
            print('-' * 60)
            print('Uma nova partida já vai começar!!')
            print('-' * 60)
        partida += 1

    # mostra o placar quando há mais de uma partida
    if n_partidas != 1:
        print('-' * 60)
        print(f'Placar final das {n_partidas} partidas ({nome1} X {nome2}): {placar_x} X {placar_o}')
        print('-' * 60)


# 5x5 jogo
def jogada_5x5(nome1, nome2, n_partidas):
    """
    (nome_jogador1, nome_jogador2, qtnd de partidas) \n
    (str, str, int) \n
    Executa o jogo da velha!!
    """
    placar_x = 0
    placar_o = 0
    partida = 1
    while partida <= n_partidas:
        if partida != 1:
            print()
            print(f'Esta é a {partida}°, okay!!? \n')
        # declaração de variáveis para lá na frente substituir por 0 ou 1
        # jogador1 == 0
        # jogador2 == 1
        a_lista = [11, 12, 13, 14, 15]
        b_lista = [21, 22, 23, 24, 25]
        c_lista = [31, 32, 33, 34, 35]
        d_lista = [41, 42, 43, 44, 45]
        e_lista = [51, 52, 53, 54, 55]

        # rodada de 9 jogadas
        print(*a_lista, sep='|')
        print(*b_lista, sep='|')
        print(*c_lista, sep='|')
        print(*d_lista, sep='|')
        print(*e_lista, sep='|')
        print()

        n_jogada = 1
        while n_jogada <= 9:
            contador = n_jogada % 2
            # se cantador != 0 -> jogada ímpar -> jogador1 -> 0
            # se cantador == 0 -> jogada par -> jogador2 -> 1
            if contador != 0:
                jogando = input(f'{nome1}, digite sua jogada linhaXcoluna (11, 21, 23, ...): ')
                # irá passar o resultado e verificar erros
                jogando = funcoes_erro.erro_5x5(a_lista, b_lista, c_lista, d_lista, e_lista, jogando)
                n_linha = jogando[0]
                n_coluna = jogando[1]
                n_linha = int(n_linha)  
                n_coluna = int(n_coluna)  
                n_coluna = n_coluna - 1  # a contagem na lista começa do 0, por isso sub(1)
                if n_linha == 1:
                    a_lista[n_coluna] = 0
                elif n_linha == 2:
                    b_lista[n_coluna] = 0
                elif n_linha == 3:
                    c_lista[n_coluna] = 0
                elif n_linha == 4:
                    d_lista[n_coluna] = 0
                elif n_linha == 5:
                    d_lista[n_coluna] = 0

            else:
                jogando = input(f'{nome2}, digite sua jogada linhaXcoluna (11, 21, 23, ...): ')
                jogando = funcoes_erro.erro_5x5(a_lista, b_lista, c_lista, d_lista, e_lista, jogando)
                n_linha = jogando[0]
                n_coluna = jogando[1]
                n_linha = int(n_linha)  
                n_coluna = int(n_coluna)  
                n_coluna = n_coluna - 1  # a contagem na lista começa do 0, por isso sub(1)
                if n_linha == 1:
                    a_lista[n_coluna] = 1
                elif n_linha == 2:
                    b_lista[n_coluna] = 1
                elif n_linha == 3:
                    c_lista[n_coluna] = 1
                elif n_linha == 4:
                    d_lista[n_coluna] = 1
                elif n_linha == 5:
                    d_lista[n_coluna] = 1
            i = 1

            # print tabuleito
            while i < 6:
                # vai passar pelas 3 listas (a_lista, b_lista,c_lista)
                # jogador1 == 0 == x
                # jogador2 == 1 == o
                if i == 1:
                    for j in a_lista:
                        if j == 0:
                            print(' x', end=' ')
                        elif j == 1:
                            print(' o', end=' ')
                        elif (j != 1) and (j != 0):
                            print(j, end=' ')
                    print()

                if i == 2:
                    for j in b_lista:
                        if j == 0:
                            print(' x', end=' ')
                        elif j == 1:
                            print(' o', end=' ')
                        elif (j != 1) and (j != 0):
                            print(j, end=' ')
                    print()

                if i == 3:
                    for j in c_lista:
                        if j == 0:
                            print(' x', end=' ')
                        elif j == 1:
                            print(' o', end=' ')
                        elif (j != 1) and (j != 0):
                            print(j, end=' ')
                    print()
                if i == 4:
                    for j in d_lista:
                        if j == 0:
                            print(' x', end=' ')
                        elif j == 1:
                            print(' o', end=' ')
                        elif (j != 1) and (j != 0):
                            print(j, end=' ')
                    print()
                if i == 5:
                    for j in d_lista:
                        if j == 0:
                            print(' x', end=' ')
                        elif j == 1:
                            print(' o', end=' ')
                        elif (j != 1) and (j != 0):
                            print(j, end=' ')
                    print()
                i += 1

            print()
            # saber se há ganhador
            win = funcoes_ganhador.ganhador_5x5(a_lista, b_lista, c_lista, d_lista, nome1, nome2)
            if win[0]:
                placar_x = placar_x + 1
                break
            elif win[1]:
                placar_o = placar_o + 1
                break
            n_jogada += 1

        # verifica se há uma nova partida ou se está na última partida
        if partida < n_partidas:
            print('-' * 60)
            print('Uma nova partida já vai começar!!')
            print('-' * 60)
        partida += 1

    # mostra o placar quando há mais de uma partida
    if n_partidas != 1:
        print('-' * 60)
        print(f'Placar final das {n_partidas} partidas ({nome1} X {nome2}): {placar_x} X {placar_o}')
        print('-' * 60)
