import play_type as play

def erro(name=str, is_input=False):
    '''

    Parameters
    ----------
    name : str, optional
        The default is str.
        it gets the player name.
    
    is_input : boolean, optional
        The default is False.
        first time that the player is puting where is his move. 

    Returns
    -------
    num : int
        if the input is valid it returns the input itself, if not it will  ask the input again.

    '''
    if is_input == True:
        try:
            num = int(input(f'{name}, digite sua jogada linhaXcoluna (11, 21, 23, ...): '))
            return num
        except ValueError:
            return erro()

    try:
        num = int(input('Número inválido, digite um outro: '))
        return num
    except ValueError:
        return erro()

def print_board(board, first_time=True):
    '''
    Parameters
    ----------
    board : list
        it prints the game board.

    Returns
    -------
    None.
    '''
    if first_time == True:
        for i in board:
            print(*i, sep='|')
            print()
    else:
        for i in board:
            for j in i:
                if j == 0: print(' x', end=' ')
                elif j == 1: print(' o', end=' ')
                elif j != 0 and j != 1: print(j, end=' ')
            print('\n')


def index_board(board, num):
    '''
    Parameters
    ----------
    board : list
        this is the board.
        
    num : int
        board house index that you want.

    Returns
    -------
    TYPE: 
        (int, int): index (line, column) of num in the board. \n
        It's also a error
    '''
    for i in board:
        if num in i:
            # line = board.index(i)
            # column =  i.index(num)
            return (board.index(i) , i.index(num))
    # num = erro()
    return index_board(board, erro())
        
def boar_menu():
    print("""
Tipos de tabuleiros:
a)3x3
b)4x4
c)5x5
            """)
    
def board():
    '''
    Returns
    -------
    board_type : str
        board type input.

    '''
    board_type = str(input('Selecione seu tabuleiro: '))
    if board_type not in 'abc':
        return board()
    return board_type

def name():
    name1 = input('Jogador 1, qual é seu nome? ')
    name2 = input('Jogador 2, qual é seu nome? ')

    if name1 == name2:
        name2 = name2 +'1'
        print(f'Vocês têm os nomes iguais, portanto, jogador 2 se chamará {name2}!!')

    print(name1 + ", você será o 'x'!")
    print(name2 + ", você será a 'o'!")
    print('-' * 60)

    return (name1, name2)

def qty_matches():
    '''
    Returns
    -------
    qty : int
        it gets how many times the players want to play.

    '''
    try:
        qty = int(input('Digite a quantidade de partidas: '))
        return qty
    except ValueError:
        return qty_matches()

def playing(board_input, player1, player2, n_matches):
    '''
    Parameters
    ----------
    board_input : str
        
    player1 : str
        player 1 name.
    player2 : TYPE
        player 2 name.
    n_matches : int

    Returns
    -------
    None.

    '''
    if board_input == 'a':
        play.board3x3(player1, player2, n_matches)
        
    elif board_input == 'b':
        play.board4x4(player1, player2, n_matches)

    elif board_input =='c':
        play.board5x5(player1, player2, n_matches)

def want_to(board_previus, name1, name2, matches):
    '''
    Parameters
    ----------
    board_previus : str

    name1 : str

    name2 : str

    matches : int

    Returns
    -------
    (bool, str, str, str, int): the wanted (play_again, board_wanted, player1, player2, qty of matches) to play again.
    

    '''
    print("OBS.: qualquer entrada diferente de 'S' ou 's' será considerada com não !!!\n")
  
    want_to_play = str(input('Deseja jogar novamente? (s, n) '))
    if want_to_play in 'Ss':
        same_name = str(input('Mesmos jogadores? (s, n) '))
        
        if same_name in 'sS':
            same_board = str(input('Mesmo tabuleiro? (s, n) '))
            
            if same_board in 'sS':
                same_qty_matches = str(input('Mesma quantia de partidas? (s, n) '))

                if same_qty_matches in 'sS':
                    return (True, board_previus, name1, name2, matches)
                
                else:
                    matches_input = qty_matches()
                    return (True, board_previus, name1, name2, matches_input)
            
            else:
                board_input = board()
                same_qty_matches = str(input('Mesma quantia de partidas? (s, n) '))

                if same_qty_matches in 'sS':
                    return (True, board_input, name1, name2, matches)
                
                else:
                    matches_input = qty_matches()
                    return (True, board_input, name1, name2, matches_input)
                
        else:
            player1, player2 = name()
            same_board = str(input('Mesmo tabuleiro? (s, n) '))
            
            if same_board in 'sS':
                same_qty_matches = str(input('Mesma quantia de partidas? (s, n) '))

                if same_qty_matches in 'sS':
                    return (True, board_previus, player1, player2, matches)
                
                else:
                    matches_input = qty_matches()
                    return (True, board_previus, player1, player2, matches_input)
                
            
            else:
                board_input = board()
                same_qty_matches = str(input('Mesma quantia de partidas? (s, n) '))

                if same_qty_matches in 'sS':
                    return (True, board_input, player1, player2, matches)
                
                else:
                    matches_input = qty_matches()
                    return (True, board_input, player1, player2, matches_input)    
                
    print('Foi um bom jogo ;-)')
    return (False, 'n/a', 'X', 'X', 0)
