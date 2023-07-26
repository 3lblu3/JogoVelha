def winner(board, type_board):
    '''
    Parameters
    ----------
    board : list \n
        this is the board itself.
    type_boar : int \n
        board type.

    Returns
    -------
    TYPE: int \n
        0: if the winner is player 1 \n
        1: if the winner is player 2
    '''
    
    if type_board == 3:
        # horizontal -> player 1
        if (board[0][0] == 0) and (board[0][1] == 0) and (board[0][2] == 0): return 0
        if (board[1][0] == 0) and (board[1][1] == 0) and (board[1][2] == 0): return 0
        if (board[2][0] == 0) and (board[2][1] == 0) and (board[2][2] == 0): return 0
        # vertical -> player 1
        if (board[0][0] == 0) and (board[1][0] == 0) and (board[2][0] == 0): return 0
        if (board[0][2] == 0) and (board[0][2] == 0) and (board[2][2] == 0): return 0
        if (board[0][1] == 0) and (board[0][1] == 0) and (board[2][1] == 0): return 0
        # diagonal -> player 1
        if (board[0][0] == 0) and (board[1][1] == 0) and (board[2][2] == 0): return 0
        if (board[0][2] == 0) and (board[1][1] == 0) and (board[2][0] == 0): return 0


        # horizontal -> player 2
        if (board[0][0] == 1) and (board[0][1] == 1) and (board[0][2] == 1): return 1
        if (board[1][0] == 1) and (board[1][1] == 1) and (board[1][2] == 1): return 1
        if (board[2][0] == 1) and (board[2][1] == 1) and (board[2][2] == 1): return 1
        # vertical -> player 2
        if (board[0][0] == 1) and (board[1][0] == 1) and (board[2][0] == 1): return 1
        if (board[0][1] == 1) and (board[0][1] == 1) and (board[2][1] == 1): return 1
        if (board[0][2] == 1) and (board[0][2] == 1) and (board[2][2] == 1): return 1
        # diagonal -> player 2
        if (board[0][0] == 1) and (board[1][1] == 1) and (board[2][2] == 1): return 1
        if (board[0][2] == 1) and (board[1][1] == 1) and (board[2][0] == 1): return 1

    if type_board == 4:
        # horizontal -> player 1
        if (board[0][0] == 0) and (board[0][1] == 0) and (board[0][2] == 0): return 0
        if (board[0][1] == 0) and (board[0][2] == 0) and (board[0][3] == 0): return 0

        if (board[1][0] == 0) and (board[1][1] == 0) and (board[1][2] == 0): return 0
        if (board[1][1] == 0) and (board[1][2] == 0) and (board[1][3] == 0): return 0

        if (board[2][0] == 0) and (board[2][1] == 0) and (board[2][2] == 0): return 0
        if (board[2][1] == 0) and (board[2][2] == 0) and (board[2][3] == 0): return 0

        if (board[3][0] == 0) and (board[3][1] == 0) and (board[3][2] == 0): return 0
        if (board[3][1] == 0) and (board[3][2] == 0) and (board[3][3] == 0): return 0

        # vertical -> player 1
        if (board[0][0] == 0) and (board[1][0] == 0) and (board[2][0] == 0): return 0
        if (board[1][0] == 0) and (board[2][0] == 0) and (board[3][0] == 0): return 0


        if (board[0][1] == 0) and (board[1][1] == 0) and (board[2][1] == 0): return 0
        if (board[1][1] == 0) and (board[2][1] == 0) and (board[3][1] == 0): return 0

        if (board[0][2] == 0) and (board[1][2] == 0) and (board[2][2] == 0): return 0
        if (board[1][2] == 0) and (board[2][2] == 0) and (board[3][2] == 0): return 0

        if (board[0][3] == 0) and (board[1][3] == 0) and (board[2][3] == 0): return 0
        if (board[1][3] == 0) and (board[2][3] == 0) and (board[3][3] == 0): return 0

        # diagonal -> player 1
        # princ. diag
        if (board[0][0] == 0) and (board[1][1] == 0) and (board[2][2] == 0): return 0
        if (board[1][1] == 0) and (board[2][2] == 0) and (board[3][3] == 0): return 0

        if (board[0][3] == 0) and (board[1][2] == 0) and (board[2][1] == 0): return 0
        if (board[1][2] == 0) and (board[2][1] == 0) and (board[3][0] == 0): return 0

        # sec. diag
        if (board[0][2] == 0) and (board[1][1] == 0) and (board[2][0] == 0): return 0
        if (board[1][3] == 0) and (board[2][2] == 0) and (board[3][1] == 0): return 0

        if (board[0][1] == 0) and (board[1][2] == 0) and (board[2][3] == 0): return 0
        if (board[1][0] == 0) and (board[2][1] == 0) and (board[3][2] == 0): return 0

    
        # horizontal -> player 2
        if (board[0][0] == 0) and (board[0][1] == 0) and (board[0][2] == 0): return 1
        if (board[0][1] == 0) and (board[0][2] == 0) and (board[0][3] == 0): return 1

        if (board[1][0] == 0) and (board[1][1] == 0) and (board[1][2] == 0): return 1
        if (board[1][1] == 0) and (board[1][2] == 0) and (board[1][3] == 0): return 1

        if (board[2][0] == 0) and (board[2][1] == 0) and (board[2][2] == 0): return 1
        if (board[2][1] == 0) and (board[2][2] == 0) and (board[2][3] == 0): return 1

        if (board[3][0] == 0) and (board[3][1] == 0) and (board[3][2] == 0): return 1
        if (board[3][1] == 0) and (board[3][2] == 0) and (board[3][3] == 0): return 1

        # vertical -> player 2
        if (board[0][0] == 0) and (board[1][0] == 0) and (board[2][0] == 0): return 1
        if (board[1][0] == 0) and (board[2][0] == 0) and (board[3][0] == 0): return 1


        if (board[0][1] == 0) and (board[1][1] == 0) and (board[2][1] == 0): return 1
        if (board[1][1] == 0) and (board[2][1] == 0) and (board[3][1] == 0): return 1

        if (board[0][2] == 0) and (board[1][2] == 0) and (board[2][2] == 0): return 1
        if (board[1][2] == 0) and (board[2][2] == 0) and (board[3][2] == 0): return 1

        if (board[0][3] == 0) and (board[1][3] == 0) and (board[2][3] == 0): return 1
        if (board[1][3] == 0) and (board[2][3] == 0) and (board[3][3] == 0): return 1

        # diagonal -> player 2
        # princ. diag
        if (board[0][0] == 0) and (board[1][1] == 0) and (board[2][2] == 0): return 1
        if (board[1][1] == 0) and (board[2][2] == 0) and (board[3][3] == 0): return 1

        if (board[0][3] == 0) and (board[1][2] == 0) and (board[2][1] == 0): return 1
        if (board[1][2] == 0) and (board[2][1] == 0) and (board[3][0] == 0): return 1

        # sec. diag
        if (board[0][2] == 0) and (board[1][1] == 0) and (board[2][0] == 0): return 1
        if (board[1][3] == 0) and (board[2][2] == 0) and (board[3][1] == 0): return 1

        if (board[0][1] == 0) and (board[1][2] == 0) and (board[2][3] == 0): return 1
        if (board[1][0] == 0) and (board[2][1] == 0) and (board[3][2] == 0): return 1

    if type_board == 5:
        # horizontal -> player 1
        if (board[0][0] == 0) and (board[0][1] == 0) and (board[0][2] == 0): return 0
        if (board[0][1] == 0) and (board[0][2] == 0) and (board[0][3] == 0): return 0
        if (board[0][2] == 0) and (board[0][3] == 0) and (board[0][4] == 0): return 0

        if (board[1][0] == 0) and (board[1][1] == 0) and (board[1][2] == 0): return 0
        if (board[1][1] == 0) and (board[1][2] == 0) and (board[1][3] == 0): return 0
        if (board[1][2] == 0) and (board[1][3] == 0) and (board[1][4] == 0): return 0

        if (board[2][0] == 0) and (board[2][1] == 0) and (board[2][2] == 0): return 0
        if (board[2][1] == 0) and (board[2][2] == 0) and (board[2][3] == 0): return 0
        if (board[2][2] == 0) and (board[2][3] == 0) and (board[2][4] == 0): return 0

        if (board[3][0] == 0) and (board[3][1] == 0) and (board[3][2] == 0): return 0
        if (board[3][1] == 0) and (board[3][2] == 0) and (board[3][3] == 0): return 0
        if (board[3][2] == 0) and (board[3][3] == 0) and (board[3][4] == 0): return 0

        if (board[4][0] == 0) and (board[4][1] == 0) and (board[4][2] == 0): return 0
        if (board[4][1] == 0) and (board[4][2] == 0) and (board[4][3] == 0): return 0
        if (board[4][2] == 0) and (board[4][3] == 0) and (board[4][4] == 0): return 0
        
        
        # vertical -> player 1
        if (board[0][0] == 0) and (board[1][0] == 0) and (board[2][0] == 0): return 0
        if (board[1][0] == 0) and (board[2][0] == 0) and (board[3][0] == 0): return 0
        if (board[2][0] == 0) and (board[3][0] == 0) and (board[4][0] == 0): return 0


        if (board[0][1] == 0) and (board[1][1] == 0) and (board[2][1] == 0): return 0
        if (board[1][1] == 0) and (board[2][1] == 0) and (board[3][1] == 0): return 0
        if (board[2][1] == 0) and (board[3][1] == 0) and (board[3][1] == 0): return 0

        if (board[0][2] == 0) and (board[1][2] == 0) and (board[2][2] == 0): return 0
        if (board[1][2] == 0) and (board[2][2] == 0) and (board[3][2] == 0): return 0
        if (board[2][2] == 0) and (board[3][2] == 0) and (board[3][2] == 0): return 0

        if (board[0][3] == 0) and (board[1][3] == 0) and (board[2][3] == 0): return 0
        if (board[1][3] == 0) and (board[2][3] == 0) and (board[3][3] == 0): return 0
        if (board[2][3] == 0) and (board[3][3] == 0) and (board[3][3] == 0): return 0

        if (board[0][4] == 0) and (board[1][4] == 0) and (board[2][4] == 0): return 0
        if (board[1][4] == 0) and (board[2][4] == 0) and (board[3][4] == 0): return 0
        if (board[2][4] == 0) and (board[3][4] == 0) and (board[3][4] == 0): return 0

        # diagonal -> player 1
        # princ. diag
        if (board[0][0] == 0) and (board[1][1] == 0) and (board[2][2] == 0): return 0
        if (board[1][1] == 0) and (board[2][2] == 0) and (board[3][3] == 0): return 0
        if (board[2][2] == 0) and (board[3][3] == 0) and (board[4][4] == 0): return 0

        if (board[0][4] == 0) and (board[1][3] == 0) and (board[2][2] == 0): return 0
        if (board[1][3] == 0) and (board[2][2] == 0) and (board[3][1] == 0): return 0
        if (board[2][2] == 0) and (board[3][1] == 0) and (board[3][0] == 0): return 0

        # sec. diag
        if (board[0][1] == 0) and (board[1][2] == 0) and (board[2][3] == 0): return 0
        if (board[1][2] == 0) and (board[2][3] == 0) and (board[3][4] == 0): return 0
        if (board[0][2] == 0) and (board[1][3] == 0) and (board[2][4] == 0): return 0

        if (board[1][0] == 0) and (board[2][1] == 0) and (board[3][2] == 0): return 0
        if (board[2][4] == 0) and (board[3][2] == 0) and (board[4][4] == 0): return 0
        if (board[2][0] == 0) and (board[3][1] == 0) and (board[4][2] == 0): return 0

        if (board[0][3] == 0) and (board[1][2] == 0) and (board[2][1] == 0): return 0
        if (board[1][2] == 0) and (board[2][1] == 0) and (board[3][0] == 0): return 0
        if (board[0][2] == 0) and (board[1][1] == 0) and (board[2][0] == 0): return 0

        if (board[1][4] == 0) and (board[2][3] == 0) and (board[3][2] == 0): return 0
        if (board[2][3] == 0) and (board[3][2] == 0) and (board[4][1] == 0): return 0
        if (board[2][4] == 0) and (board[3][3] == 0) and (board[4][2] == 0): return 0


        # horizontal -> player 2
        if (board[0][0] == 0) and (board[0][1] == 0) and (board[0][2] == 0): return 1
        if (board[0][1] == 0) and (board[0][2] == 0) and (board[0][3] == 0): return 1
        if (board[0][2] == 0) and (board[0][3] == 0) and (board[0][4] == 0): return 1

        if (board[1][0] == 0) and (board[1][1] == 0) and (board[1][2] == 0): return 1
        if (board[1][1] == 0) and (board[1][2] == 0) and (board[1][3] == 0): return 1
        if (board[1][2] == 0) and (board[1][3] == 0) and (board[1][4] == 0): return 1

        if (board[2][0] == 0) and (board[2][1] == 0) and (board[2][2] == 0): return 1
        if (board[2][1] == 0) and (board[2][2] == 0) and (board[2][3] == 0): return 1
        if (board[2][2] == 0) and (board[2][3] == 0) and (board[2][4] == 0): return 1

        if (board[3][0] == 0) and (board[3][1] == 0) and (board[3][2] == 0): return 1
        if (board[3][1] == 0) and (board[3][2] == 0) and (board[3][3] == 0): return 1
        if (board[3][2] == 0) and (board[3][3] == 0) and (board[3][4] == 0): return 1

        if (board[4][0] == 0) and (board[4][1] == 0) and (board[4][2] == 0): return 1
        if (board[4][1] == 0) and (board[4][2] == 0) and (board[4][3] == 0): return 1
        if (board[4][2] == 0) and (board[4][3] == 0) and (board[4][4] == 0): return 1
        
        
        # vertical -> player 2
        if (board[0][0] == 0) and (board[1][0] == 0) and (board[2][0] == 0): return 1
        if (board[1][0] == 0) and (board[2][0] == 0) and (board[3][0] == 0): return 1
        if (board[2][0] == 0) and (board[3][0] == 0) and (board[4][0] == 0): return 1


        if (board[0][1] == 0) and (board[1][1] == 0) and (board[2][1] == 0): return 1
        if (board[1][1] == 0) and (board[2][1] == 0) and (board[3][1] == 0): return 1
        if (board[2][1] == 0) and (board[3][1] == 0) and (board[3][1] == 0): return 1

        if (board[0][2] == 0) and (board[1][2] == 0) and (board[2][2] == 0): return 1
        if (board[1][2] == 0) and (board[2][2] == 0) and (board[3][2] == 0): return 1
        if (board[2][2] == 0) and (board[3][2] == 0) and (board[3][2] == 0): return 1

        if (board[0][3] == 0) and (board[1][3] == 0) and (board[2][3] == 0): return 1
        if (board[1][3] == 0) and (board[2][3] == 0) and (board[3][3] == 0): return 1
        if (board[2][3] == 0) and (board[3][3] == 0) and (board[3][3] == 0): return 1

        if (board[0][4] == 0) and (board[1][4] == 0) and (board[2][4] == 0): return 1
        if (board[1][4] == 0) and (board[2][4] == 0) and (board[3][4] == 0): return 1
        if (board[2][4] == 0) and (board[3][4] == 0) and (board[3][4] == 0): return 1

        # diagonal -> player 2
        # princ. diag
        if (board[0][0] == 0) and (board[1][1] == 0) and (board[2][2] == 0): return 1
        if (board[1][1] == 0) and (board[2][2] == 0) and (board[3][3] == 0): return 1
        if (board[2][2] == 0) and (board[3][3] == 0) and (board[4][4] == 0): return 1

        if (board[0][4] == 0) and (board[1][3] == 0) and (board[2][2] == 0): return 1
        if (board[1][3] == 0) and (board[2][2] == 0) and (board[3][1] == 0): return 1
        if (board[2][2] == 0) and (board[3][1] == 0) and (board[3][0] == 0): return 1

        # sec. diag
        if (board[0][1] == 0) and (board[1][2] == 0) and (board[2][3] == 0): return 1
        if (board[1][2] == 0) and (board[2][3] == 0) and (board[3][4] == 0): return 1
        if (board[0][2] == 0) and (board[1][3] == 0) and (board[2][4] == 0): return 1

        if (board[1][0] == 0) and (board[2][1] == 0) and (board[3][2] == 0): return 1
        if (board[2][4] == 0) and (board[3][2] == 0) and (board[4][4] == 0): return 1
        if (board[2][0] == 0) and (board[3][1] == 0) and (board[4][2] == 0): return 1

        if (board[0][3] == 0) and (board[1][2] == 0) and (board[2][1] == 0): return 1
        if (board[1][2] == 0) and (board[2][1] == 0) and (board[3][0] == 0): return 1
        if (board[0][2] == 0) and (board[1][1] == 0) and (board[2][0] == 0): return 1

        if (board[1][4] == 0) and (board[2][3] == 0) and (board[3][2] == 0): return 1
        if (board[2][3] == 0) and (board[3][2] == 0) and (board[4][1] == 0): return 1
        if (board[2][4] == 0) and (board[3][3] == 0) and (board[4][2] == 0): return 1
