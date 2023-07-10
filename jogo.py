def index_tab(tabuleiro, num):
    for i in tabuleiro:
        if num in i:
            casa_num =  i.index(num)
            return (tabuleiro.index(i), casa_num)
        
def print_tab(tabuleiro):
    for i in tabuleiro:
        print(*i, sep='|')
    print()
