import jogo_funcoes
# teste
print("Bem-vindo(a,e) ao Jogo da Velha GTHC")
print("Tipo de jogo: \n" + "a) 3X3 \n" + "b) 4X4 \nc) 5x5")

tipodejogo = input("Selecione a letra respectiva ao seu modo de jogo: ")
n_partidas = int(input("Digite o número de partidas: "))
nome1 = input("Qual é o seu nome? ")
nome2 = input("Qual é o seu nome? ")

def menu(tipodejogo, nome1, nome2):
    if nome2 == nome1:
        print(f"{nome2}, você tem o mesmo nome que o 1°Jogador")
        nome2 = nome2 + "1"
        print(f"Assim, {nome1}, você será renomeado {nome2}, Okay!!?")
        print(nome1 + ", você será o 'x'!")
        print(nome2 + ", você será a 'o'!")
    else:
        print(nome1 + ", você será o 'x'!")
        print(nome2 + ", você será a 'o'!")
    print('-' * 60)
    
    jogo = 0
    if tipodejogo in "Aa":
        jogo_funcoes.jogada_3x3(nome1, nome2, n_partidas)
        while jogo == 0:
            jogar_nov = input('Deseja jogar novamente? (s/n) ')
            if jogar_nov in "Ss":  
                jogadores_nov = input('São os mesmos jogadores? (s/n) ')
                if jogadores_nov in "Ss":
                    jogo_funcoes.jogada_3x3(nome1, nome2, n_partidas)
                    print('-' * 60)
                else:
                    nome1 = input("Qual é o seu nome? ")
                    nome2 = input("Qual é o seu nome? ")
                    print(nome1 + ", você será o 'x'!")
                    print(nome1 + ", você será a 'o'!")
                    print('-' * 60)
                    jogo_funcoes.jogada_3x3(nome1, nome2, n_partidas)
            else:
                break
                
    elif tipodejogo in "Bb":
        jogo_funcoes.jogada_4x4(nome1, nome2, n_partidas)
        while jogo == 0:
            jogar_nov = input('Deseja jogar novamente? (s/n) ')
            if jogar_nov in "Ss":  
                jogadores_nov = input('São os mesmos jogadores? (s/n) ')
                if jogadores_nov in "Ss":
                    jogo_funcoes.jogada_4x4(nome1, nome2, n_partidas)
                    print('-' * 60)
                else:
                    nome1 = input("Qual é o seu nome? ")
                    nome2 = input("Qual é o seu nome? ")
                    print(nome1 + ", você será o 'x'!")
                    print(nome1 + ", você será a 'o'!")
                    print('-' * 60)
                    jogo_funcoes.jogada_4x4(nome1, nome2, n_partidas)
            else:
                break
                
    elif tipodejogo in "Cc":
        jogo_funcoes.jogada_5x5(nome1, nome2, n_partidas)
        while jogo == 0:
            jogar_nov = input('Deseja jogar novamente? (s/n) ')
            if jogar_nov in "Ss":  
                jogadores_nov = input('São os mesmos jogadores? (s/n) ')
                if jogadores_nov in "Ss":
                    jogo_funcoes.jogada_5x5(nome1, nome2, n_partidas)
                    print('-' * 60)
                else:
                    nome1 = input("Qual é o seu nome? ")
                    nome2 = input("Qual é o seu nome? ")
                    print(nome1 + ", você será o 'x'!")
                    print(nome1 + ", você será a 'o'!")
                    print('-' * 60)
                    jogo_funcoes.jogada_5x5(nome1, nome2, n_partidas)
            else:
                break

    elif tipodejogo not in "AaBbCc":
        tipodejogo = input('Alternativa inválida!! Digite novamente:')
        menu(tipodejogo, nome1, nome2)

menu(tipodejogo, nome1, nome2)
