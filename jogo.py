def index_tab(tabuleiro, num):
    '''
    Parameters
    ----------
    tabuleiro : list
        this the board.
        
    num : TYPE
        board house index that you want.

    Returns
    -------
    TYPE: (int, int)
        index of num in tabuleiro.
    '''
    for i in tabuleiro:
        if num in i:
            casa_num =  i.index(num)
            return (tabuleiro.index(i), casa_num)
        
def print_tab(tabuleiro):
    '''
    Parameters
    ----------
    tabuleiro : list
        it prints the game board.

    Returns
    -------
    None.
    '''
    for i in tabuleiro:
        print(*i, sep='|')
    print()
