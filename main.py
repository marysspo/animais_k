from random import choice

animais = ['gato', 'cachorro', 'vaca', 'galinha', 'cobra', 'sapo', 'borboleta']#cores
veiculos = ['carro', 'moto', 'avião', 'bike', 'navio', 'onibus']
TENTATIVA = 0

esc = int(input('''\nEscolhe qual categoria que:\n
1) Animais
2) Veiculos
--> '''))

if esc == 1:
    print('\nEstas são os itens do jogo')
    for e in animais:
        print(f'-> {e}')

    escolha_geral = choice(animais)

    while TENTATIVA < 3:
        ESCOLHA = str(input('Qual sua jogada: '))
        ESCOLHA = ESCOLHA.lower()
        if escolha_geral == ESCOLHA:
            print('Voce acertou')
            break
        elif escolha_geral != ESCOLHA and escolha_geral in animais:
            print('\nVoce errou')
            TENTATIVA += 1
            print(f'TENTATIVA {TENTATIVA}\n')
        else:
            print('Resposta invalida\n')

if esc == 2:
    print('Estas são os itens do jogo')
    for e in veiculos:
        print(f'-> {e}')

    escolha_geral = choice(veiculos)

    while TENTATIVA < 3:
        ESCOLHA = str(input('Qual sua jogada: '))
        ESCOLHA = ESCOLHA.lower()
        if escolha_geral == ESCOLHA:
            print('Voce acertou')
        elif escolha_geral != ESCOLHA and escolha_geral in veiculos:
            print('\nVoce errou')
            TENTATIVA += 1
            print(f'TENTATIVA {TENTATIVA}\n')
        else:
            print('Resposta invalida\n')