import utils
import winner

def board3x3(name1, name2, n_matches):
    # player 1 == 0 == x
    # player 2 == 1 == o
    score_x = 0
    score_o = 0
    for i in range(n_matches):
        board = [[11, 12, 13], 
                 [21, 22, 23], 
                 [31, 32, 33]]
        print(f'Esta é a {i + 1}°, okay!!? \n')
        utils.print_board(board)

        play_qty = 0
        while play_qty < 9:
            player = play_qty % 2
            if player == 0:
                playing = utils.erro(name=name1, is_input=True)
                move = utils.index_board(board, playing)
                board[move[0]][move[1]] = 0

            else:
                playing = utils.erro(name=name2, is_input=True)
                move = utils.index_board(board, playing)
                board[move[0]][move[1]] = 1
            utils.print_board(board, first_time=False)

            # is there a winner?
            winner_match = winner.winner(board, 3)
            if winner_match == 0:
                score_x += 1
                print(f'{name1}, você ganhou essa partida!!')
                break
            elif winner_match == 1:
                score_o += 1
                print(f'{name2}, você ganhou essa partida!!')
                break

            play_qty += 1
            if play_qty == 8: print('Deu velha!!!')
            # qty_moves == {0 < moves < 8} = 9 elements

        # a new match will begin
        if n_matches != 1 and i < n_matches - 1:
            print('-' * 60)
            print('Uma nova partida já vai começar!!')
            print('-' * 60)

    # Final score
    print('-' * 60)
    print(f'Placar final da(s) {n_matches} partida(s) ({name1} X {name2}): {score_x} X {score_o}')
    print('-' * 60)


def board4x4(name1, name2, n_matches):
    # player 1 == 0 == x
    # player 2 == 1 == o
    score_x = 0
    score_o = 0
    for i in range(n_matches):
        board =  [[11, 12, 13, 14], 
                  [21, 22, 23, 24], 
                  [31, 32, 33, 34], 
                  [41, 42, 43, 44]]
        print(f'Esta é a {i + 1}°, okay!!? \n')
        utils.print_board(board)

        play_qty = 0
        while play_qty < 16:
            player = play_qty % 2
            if player == 0:
                playing = utils.erro(name=name1, is_input=True)
                move = utils.index_board(board, playing)
                board[move[0]][move[1]] = 0

            else:
                playing = utils.erro(name=name2, is_input=True)
                move = utils.index_board(board, playing)
                board[move[0]][move[1]] = 1
            utils.print_board(board, first_time=False)

            # is there a winner?
            winner_match = winner.winner(board, 4)
            if winner_match == 0:
                score_x += 1
                print(f'{name1}, você ganhou essa partida!!')
                break
            elif winner_match == 1:
                score_o += 1
                print(f'{name2}, você ganhou essa partida!!')
                break

            play_qty += 1
            if play_qty == 15: print('Deu velha!!!')
            # qty_moves == {0 < moves < 8} = 9 elements

        # a new match will begin
        if n_matches != 1 and i < n_matches - 1:
            print('-' * 60)
            print('Uma nova partida já vai começar!!')
            print('-' * 60)

    # Final score
    print('-' * 60)
    print(f'Placar final da(s) {n_matches} partida(s) ({name1} X {name2}): {score_x} X {score_o}')
    print('-' * 60)


def board5x5(name1, name2, n_matches):
    # player 1 == 0 == x
    # player 2 == 1 == o
    score_x = 0
    score_o = 0
    for i in range(n_matches):
        board = [[11, 12, 13, 14, 15], 
                 [21, 22, 23, 24, 25], 
                 [31, 32, 33, 34, 35], 
                 [41, 42, 43, 44, 45],
                 [51, 52, 53, 54, 55]]
        print(f'Esta é a {i + 1}°, okay!!? \n')
        utils.print_board(board)

        play_qty = 0
        while play_qty < 9:
            player = play_qty % 2
            if player == 0:
                playing = utils.erro(name=name1, is_input=True)
                move = utils.index_board(board, playing)
                board[move[0]][move[1]] = 0

            else:
                playing = utils.erro(name=name2, is_input=True)
                move = utils.index_board(board, playing)
                board[move[0]][move[1]] = 1
            utils.print_board(board, first_time=False)

            # is there a winner?
            winner_match = winner.winner(board, 5)
            if winner_match == 0:
                score_x += 1
                print(f'{name1}, você ganhou essa partida!!')
                break
            elif winner_match == 1:
                score_o += 1
                print(f'{name2}, você ganhou essa partida!!')
                break

            play_qty += 1
            if play_qty == 24: print('Deu velha!!!')
            # qty_moves == {0 < moves < 8} = 9 elements

        # a new match will begin
        if n_matches != 1 and i < n_matches - 1:
            print('-' * 60)
            print('Uma nova partida já vai começar!!')
            print('-' * 60)

    # Final score
    print('-' * 60)
    print(f'Placar final da(s) {n_matches} partida(s) ({name1} X {name2}): {score_x} X {score_o}')
    print('-' * 60)
