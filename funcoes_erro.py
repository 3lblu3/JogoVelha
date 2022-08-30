def erro_3x3(a_lista, b_lista, c_lista, verificacao):
    """verifica se a casa já foi preenchida ou se o 'input' está de acordo com o que se foi pedido"""
    # to-do:
    # fazer essa função ler qualquer tabuleiro (3x3,4x4x,5x5)

    # erro: ver se há só números
    alfabeto_minusculas = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h',
                           'j', 'k', 'l', 'ç', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
    alfabeto_maiusculas = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H',
                           'J', 'K', 'L', 'Ç', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']

    alfabeto_minusculas_acentuadas = ['á', 'é', 'í', 'ó', 'ú', 'à', 'è', 'ì', 'ò', 'ù', 'â', 'ê', 'î', 'ô', 'û', 'ã',
                                      'õ']
    alfabeto_maiusculas_acentuadas = ['Á', 'É', 'Í', 'Ó', 'Ú', 'À', 'È', 'Ì', 'Ò', 'Ù', 'Â', 'Ê', 'Î', 'Ô', 'Û', 'Ã',
                                      'Õ']
    alfabeto_caracteres = ['"', "'", '!', '@', '#', '$', '%', '¨', '&', '*', '(', ')', '_', '-', '+', '=', '¹', '²',
                           '³', '£', '¢', '¬', '§', "|", '<', ",", '.', '>', ';', ':', '/', '?', '°', '^', '~', '}',
                           ']', 'º', '`', '´', '{', '[', 'ª', ' ']

    erro_letras = 0

    for letra_verificando in verificacao:
        if (letra_verificando in alfabeto_minusculas) or (letra_verificando in alfabeto_maiusculas) or (
                letra_verificando in alfabeto_minusculas_acentuadas) or (
                letra_verificando in alfabeto_maiusculas_acentuadas) or (letra_verificando in alfabeto_caracteres):
            erro_letras += 1

    if erro_letras != 0:
        jogando = input('Por favor, somente números: ')
        return erro_3x3(a_lista, b_lista, c_lista, jogando)

    # erro: ver se é um número válido e se é uma casa do jogo

    # esse try e except é porque toda vez que o input era \ ele não lia como caractere
    # digia que não dava para converter \ para int
    # (não achei uma maneira de converte \ para uma string e veridicar \ em 'if erro_letras != 0:')
    # isso se dava ao fato de não conseguir colocar o \ para ser lido como caractere
    # fazendo esse try e except resolvemos esse problema com o \ não ser lido como caractere
    try:
        num_verificador = int(verificacao)
    except:
        jogando = input('Por favor, somente somente números: ')
        return erro_3x3(a_lista, b_lista, c_lista, jogando)

    casas_3x3 = [11, 12, 13, 21, 22, 23, 31, 32, 33]

    if num_verificador not in casas_3x3:
        jogando = input('Você digitou uma casa inválida, digite uma nova: ')
        return erro_3x3(a_lista, b_lista, c_lista, verificacao)

    # erro: verificar se a casa está livre

    # OBS.: 0 == x ; 1 == o
    # se há 0 ou 1 naquela posição da linha, pegamos o seu index(posição na lista) e colocamos na lista_index
    # se já houver esse index na lista ele pula(continue), caso contrário ele faz um append
    # para verificar se a casa já foi preenchida, ele vê se o num digitado está na lista casa_3x3
    # e se o index desse num na lista casas_3x3 está na lista_index
    # se isso for verdade é porque a casa já foi preenchida
    lista_index = []

    for a in a_lista:
        if (a == 1) or (a == 0):
            # aqui eu vou descobrir o index para saber qual é a num da casa
            # index(letra) -> letra é o num que quero saber o index na lista original
            if a_lista.index(a) == 0:
                casa = 10 + 1
                index_da_casa = casas_3x3.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

            elif a_lista.index(a) == 1:
                casa = 10 + 2
                index_da_casa = casas_3x3.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

            elif a_lista.index(a) == 2:
                casa = 10 + 3
                index_da_casa = casas_3x3.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

    for b in b_lista:
        if (b == 1) or (b == 0):
            # aqui eu vou descobrir o index para saber qual é a num da casa
            # index(letra) -> letra é o num que quero saber o index na lista original
            if b_lista.index(b) == 0:
                casa = 20 + 1
                index_da_casa = casas_3x3.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

            elif b_lista.index(b) == 1:
                casa = 20 + 2
                index_da_casa = casas_3x3.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

            elif b_lista.index(b) == 2:
                casa = 20 + 3
                index_da_casa = casas_3x3.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

    for c in c_lista:
        if (c == 1) or (c == 0):
            # aqui eu vou descobrir o index para saber qual é a num da casa
            # index(letra) -> letra é o num que quero saber o index na lista original
            if c_lista.index(c) == 0:
                casa = 30 + 1
                index_da_casa = casas_3x3.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

            elif c_lista.index(c) == 1:
                casa = 30 + 2
                index_da_casa = casas_3x3.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

            elif c_lista.index(c) == 2:
                casa = 30 + 3
                index_da_casa = casas_3x3.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

    if (num_verificador in casas_3x3) and ((casas_3x3.index(num_verificador)) in lista_index):
        jogando = input('Essa casa já foi preenchida, digite outra: ')
        return erro_3x3(a_lista, b_lista, c_lista, jogando)

    jogando = verificacao
    return jogando


def erro_4x4(a_lista, b_lista, c_lista, d_lista, verificacao):
    """verifica se a casa já foi preenchida ou se o 'input' está de acordo com o que se foi pedido"""
    # to-do:
    # fazer essa função ler qualquer tabuleiro (3x3,4x4x,5x5)

    # erro: ver se há só números
    alfabeto_minusculas = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h',
                           'j', 'k', 'l', 'ç', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
    alfabeto_maiusculas = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H',
                           'J', 'K', 'L', 'Ç', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']

    alfabeto_minusculas_acentuadas = ['á', 'é', 'í', 'ó', 'ú', 'à', 'è', 'ì', 'ò', 'ù', 'â', 'ê', 'î', 'ô', 'û', 'ã',
                                      'õ']
    alfabeto_maiusculas_acentuadas = ['Á', 'É', 'Í', 'Ó', 'Ú', 'À', 'È', 'Ì', 'Ò', 'Ù', 'Â', 'Ê', 'Î', 'Ô', 'Û', 'Ã',
                                      'Õ']
    alfabeto_caracteres = ['"', "'", '!', '@', '#', '$', '%', '¨', '&', '*', '(', ')', '_', '-', '+', '=', '¹', '²',
                           '³', '£', '¢', '¬', '§', "|", '<', ",", '.', '>', ';', ':', '/', '?', '°', '^', '~', '}',
                           ']', 'º', '`', '´', '{', '[', 'ª', ' ']

    erro_letras = 0

    for letra_verificando in verificacao:
        if (letra_verificando in alfabeto_minusculas) or (letra_verificando in alfabeto_maiusculas) or (
                letra_verificando in alfabeto_minusculas_acentuadas) or (
                letra_verificando in alfabeto_maiusculas_acentuadas) or (letra_verificando in alfabeto_caracteres):
            erro_letras += 1

    if erro_letras != 0:
        jogando = input('Por favor, somente somente números: ')
        return erro_4x4(a_lista, b_lista, c_lista, d_lista, jogando)

    # erro: ver se é um número válido e se é uma casa do jogo

    # esse try e except é porque toda vez que o input era \ ele não lia como caractere
    # digia que não dava para converter \ para int
    # (não achei uma maneira de converte \ para uma string e veridicar \ em 'if erro_letras != 0:')
    # isso se dava ao fato de não conseguir colocar o \ para ser lido como caractere
    # fazendo esse try e except resolvemos esse problema com o \ não ser lido como caractere
    try:
        num_verificador = int(verificacao)
    except:
        jogando = input('Por favor, soment somente números: ')
        return erro_4x4(a_lista, b_lista, c_lista, d_lista, jogando)

    casas_4x4 = [11, 12, 13, 14, 21, 22, 23, 24, 31, 32, 33, 34, 41, 42, 43, 44]

    if num_verificador not in casas_4x4:
        jogando = input('Você digitou uma casa inválida, digite uma nova: ')
        return erro_4x4(a_lista, b_lista, c_lista, d_lista, jogando)

    # erro: verificar se a casa está livre

    # OBS.: 0 == x ; 1 == o
    # se há 0 ou 1 naquela posição da linha, pegamos o seu index(posição na lista) e colocamos na lista_index
    # se já houver esse index na lista ele pula(continue), caso contrário ele faz um append
    # para verificar se a casa já foi preenchida, ele vê se o num digitado está na lista casa_3x3
    # e se o index desse num na lista casas_3x3 está na lista_index
    # se isso for verdade é porque a casa já foi preenchida
    lista_index = []

    for a in a_lista:
        if (a == 1) or (a == 0):
            # aqui eu vou descobrir o index para saber qual é a num da casa
            # index(letra) -> letra é o num que quero saber o index na lista original
            if a_lista.index(a) == 0:
                casa = 10 + 1
                index_da_casa = casas_4x4.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

            elif a_lista.index(a) == 1:
                casa = 10 + 2
                index_da_casa = casas_4x4.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

            elif a_lista.index(a) == 2:
                casa = 10 + 3
                index_da_casa = casas_4x4.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

            elif a_lista.index(a) == 3:
                casa = 10 + 4
                index_da_casa = casas_4x4.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

    for b in b_lista:
        if (b == 1) or (b == 0):
            # aqui eu vou descobrir o index para saber qual é a num da casa
            # index(letra) -> letra é o num que quero saber o index na lista original
            if b_lista.index(b) == 0:
                casa = 20 + 1
                index_da_casa = casas_4x4.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

            elif b_lista.index(b) == 1:
                casa = 20 + 2
                index_da_casa = casas_4x4.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

            elif b_lista.index(b) == 2:
                casa = 20 + 3
                index_da_casa = casas_4x4.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

            elif b_lista.index(b) == 3:
                casa = 20 + 4
                index_da_casa = casas_4x4.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

    for c in c_lista:
        if (c == 1) or (c == 0):
            # aqui eu vou descobrir o index para saber qual é a num da casa
            # index(letra) -> letra é o num que quero saber o index na lista original
            if c_lista.index(c) == 0:
                casa = 30 + 1
                index_da_casa = casas_4x4.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

            elif c_lista.index(c) == 1:
                casa = 30 + 2
                index_da_casa = casas_4x4.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

            elif c_lista.index(c) == 2:
                casa = 30 + 3
                index_da_casa = casas_4x4.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

            elif c_lista.index(c) == 3:
                casa = 30 + 4
                index_da_casa = casas_4x4.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

    for d in d_lista:
        if (d == 1) or (d == 0):
            # aqui eu vou descobrir o index para saber qual é a num da casa
            # index(letra) -> letra é o num que quero saber o index na lista original
            if d_lista.index(d) == 0:
                casa = 40 + 1
                index_da_casa = casas_4x4.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

            elif d_lista.index(d) == 1:
                casa = 40 + 2
                index_da_casa = casas_4x4.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

            elif d_lista.index(d) == 2:
                casa = 40 + 3
                index_da_casa = casas_4x4.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

            elif d_lista.index(d) == 3:
                casa = 40 + 4
                index_da_casa = casas_4x4.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

    if (num_verificador in casas_4x4) and (casas_4x4.index(num_verificador) in lista_index):
        jogando = input('Essa casa já foi preenchida, digite outra: ')
        return erro_4x4(a_lista, b_lista, c_lista, d_lista, jogando)

    jogando = verificacao
    return jogando


def erro_5x5(a_lista, b_lista, c_lista, d_lista, e_lista, verificacao):
    """verifica se a casa já foi preenchida ou se o 'input' está de acordo com o que se foi pedido"""
    # to-do:
    # fazer essa função ler qualquer tabuleiro (3x3,4x4x,5x5)

    # erro: ver se há só números
    alfabeto_minusculas = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h',
                           'j', 'k', 'l', 'ç', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
    alfabeto_maiusculas = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H',
                           'J', 'K', 'L', 'Ç', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']

    alfabeto_minusculas_acentuadas = ['á', 'é', 'í', 'ó', 'ú', 'à', 'è', 'ì', 'ò', 'ù', 'â', 'ê', 'î', 'ô', 'û', 'ã',
                                      'õ']
    alfabeto_maiusculas_acentuadas = ['Á', 'É', 'Í', 'Ó', 'Ú', 'À', 'È', 'Ì', 'Ò', 'Ù', 'Â', 'Ê', 'Î', 'Ô', 'Û', 'Ã',
                                      'Õ']
    alfabeto_caracteres = ['"', "'", '!', '@', '#', '$', '%', '¨', '&', '*', '(', ')', '_', '-', '+', '=', '¹', '²',
                           '³', '£', '¢', '¬', '§', "|", '<', ",", '.', '>', ';', ':', '/', '?', '°', '^', '~', '}',
                           ']', 'º', '`', '´', '{', '[', 'ª', ' ']

    erro_letras = 0

    for letra_verificando in verificacao:
        if (letra_verificando in alfabeto_minusculas) or (letra_verificando in alfabeto_maiusculas) or (
                letra_verificando in alfabeto_minusculas_acentuadas) or (
                letra_verificando in alfabeto_maiusculas_acentuadas) or (letra_verificando in alfabeto_caracteres):
            erro_letras += 1

    if erro_letras != 0:
        jogando = input('Por favor, somente somente números: ')
        return erro_5x5(a_lista, b_lista, c_lista, d_lista, e_lista, jogando)

    # erro: ver se é um número válido e se é uma casa do jogo

    # esse try e except é porque toda vez que o input era \ ele não lia como caractere
    # digia que não dava para converter \ para int
    # (não achei uma maneira de converte \ para uma string e veridicar \ em 'if erro_letras != 0:')
    # isso se dava ao fato de não conseguir colocar o \ para ser lido como caractere
    # fazendo esse try e except resolvemos esse problema com o \ não ser lido como caractere
    try:
        num_verificador = int(verificacao)
    except:
        jogando = input('Por favor, soment somente números: ')
        return erro_5x5(a_lista, b_lista, c_lista, d_lista, e_lista, jogando)

    casas_5x5 = [11, 12, 13, 14, 15, 21, 22, 23, 24, 25, 31, 32, 33, 34, 35, 51, 52, 53, 54, 55]

    if num_verificador not in casas_5x5:
        jogando = input('Você digitou uma casa inválida, digite uma nova: ')
        return erro_5x5(a_lista, b_lista, c_lista, d_lista, e_lista, jogando)

    # erro: verificar se a casa está livre

    # OBS.: 0 == x ; 1 == o
    # se há 0 ou 1 naquela posição da linha, pegamos o seu index(posição na lista) e colocamos na lista_index
    # se já houver esse index na lista ele pula(continue), caso contrário ele faz um append
    # para verificar se a casa já foi preenchida, ele vê se o num digitado está na lista casa_3x3
    # e se o index desse num na lista casas_3x3 está na lista_index
    # se isso for verdade é porque a casa já foi preenchida
    lista_index = []

    for a in a_lista:
        if (a == 1) or (a == 0):
            # aqui eu vou descobrir o index para saber qual é a num da casa
            # index(letra) -> letra é o num que quero saber o index na lista original
            if a_lista.index(a) == 0:
                casa = 10 + 1
                index_da_casa = casas_5x5.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

            elif a_lista.index(a) == 1:
                casa = 10 + 2
                index_da_casa = casas_5x5.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

            elif a_lista.index(a) == 2:
                casa = 10 + 3
                index_da_casa = casas_5x5.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

            elif a_lista.index(a) == 3:
                casa = 10 + 4
                index_da_casa = casas_5x5.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue
            elif a_lista.index(a) == 4:
                casa = 10 + 5
                index_da_casa = casas_5x5.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

    for b in b_lista:
        if (b == 1) or (b == 0):
            # aqui eu vou descobrir o index para saber qual é a num da casa
            # index(letra) -> letra é o num que quero saber o index na lista original
            if b_lista.index(b) == 0:
                casa = 20 + 1
                index_da_casa = casas_5x5.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

            elif b_lista.index(b) == 1:
                casa = 20 + 2
                index_da_casa = casas_5x5.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

            elif b_lista.index(b) == 2:
                casa = 20 + 3
                index_da_casa = casas_5x5.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

            elif b_lista.index(b) == 3:
                casa = 20 + 4
                index_da_casa = casas_5x5.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

            elif b_lista.index(b) == 4:
                casa = 20 + 5
                index_da_casa = casas_5x5.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

    for c in c_lista:
        if (c == 1) or (c == 0):
            # aqui eu vou descobrir o index para saber qual é a num da casa
            # index(letra) -> letra é o num que quero saber o index na lista original
            if c_lista.index(c) == 0:
                casa = 30 + 1
                index_da_casa = casas_5x5.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

            elif c_lista.index(c) == 1:
                casa = 30 + 2
                index_da_casa = casas_5x5.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

            elif c_lista.index(c) == 2:
                casa = 30 + 3
                index_da_casa = casas_5x5.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

            elif c_lista.index(c) == 3:
                casa = 30 + 4
                index_da_casa = casas_5x5.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

            elif c_lista.index(c) == 4:
                casa = 30 + 5
                index_da_casa = casas_5x5.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

    for d in d_lista:
        if (d == 1) or (d == 0):
            # aqui eu vou descobrir o index para saber qual é a num da casa
            # index(letra) -> letra é o num que quero saber o index na lista original
            if d_lista.index(d) == 0:
                casa = 40 + 1
                index_da_casa = casas_5x5.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

            elif d_lista.index(d) == 1:
                casa = 40 + 2
                index_da_casa = casas_5x5.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

            elif d_lista.index(d) == 2:
                casa = 40 + 3
                index_da_casa = casas_5x5.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

            elif d_lista.index(d) == 3:
                casa = 40 + 4
                index_da_casa = casas_5x5.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

            elif d_lista.index(d) == 4:
                casa = 40 + 5
                index_da_casa = casas_5x5.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

    for e in e_lista:
        if (e == 1) or (e == 0):
            # aqui eu vou descobrir o index para saber qual é a num da casa
            # index(letra) -> letra é o num que quero saber o index na lista original
            if e_lista.index(e) == 0:
                casa = 50 + 1
                index_da_casa = casas_5x5.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

            elif e_lista.index(e) == 1:
                casa = 50 + 2
                index_da_casa = casas_5x5.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

            elif e_lista.index(e) == 2:
                casa = 50 + 3
                index_da_casa = casas_5x5.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

            elif e_lista.index(e) == 3:
                casa = 50 + 4
                index_da_casa = casas_5x5.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

            elif e_lista.index(e) == 4:
                casa = 50 + 5
                index_da_casa = casas_5x5.index(casa)  # index da casa na lista casa_3x3
                if index_da_casa not in lista_index:  # verifico se já há esse elemento na lista
                    lista_index.append(index_da_casa)
                else:
                    continue

    if (num_verificador in casas_5x5) and (casas_5x5.index(num_verificador) in lista_index):
        jogando = input('Essa casa já foi preenchida, digite outra: ')
        return erro_5x5(a_lista, b_lista, c_lista, d_lista, e_lista, jogando)

    jogando = verificacao
    return jogando