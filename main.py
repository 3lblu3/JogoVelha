import utils

print("Bem-vindo ao Jogo da Velha!!!")

def main():
    first_run = True
    play_again = True
    utils.boar_menu()
    while play_again == True:
        if first_run == True:
            board_input = utils.board()
            player1, player2 = utils.name()
            matches = utils.qty_matches()

            utils.playing(board_input, player1, player2, matches)
            first_run = False

        else:
            play_again, board_input, player1, player2, matches = utils.want_to(board_input, player1, player2, matches)
            if play_again == False: break
            utils.playing(board_input, player1, player2, matches)

main()
