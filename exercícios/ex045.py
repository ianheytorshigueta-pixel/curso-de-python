"""Crie um programa que faça o computador jogar Jokenpô com você."""

from random import randint
acoes = ['Pedra', 'Papel', 'Tesoura']
jogador = int(input('Suas opções:'
                    '\n[ 0 ] PEDRA'
                    '\n[ 1 ] PAPEL'
                    '\n[ 2 ] TESOURA'
                    '\nQual é a sua jogada? '))
compt = randint(0, 2)
if 0 <= jogador <= 2:
    print('-='*20)
    print(f'Computador jogou {acoes[compt]}'
        f'\nJogador jogou {acoes[jogador]}')
    print('-='*20)
    if jogador != compt:
        resultado = ''
        if jogador == 0 and compt == 1:
            resultado = False
        elif jogador == 0 and compt == 2:
            resultado = True
        elif jogador == 1 and compt == 0:
            resultado = True
        elif jogador == 1 and compt == 2:
            resultador = False
        elif jogador == 2 and compt == 0:
            resultado = False
        else:
            resultado = True
        if resultado == True:
            print('JOGADOR VENCEU!')
        else:
            print('COMPUTADOR VENCEU!')
    else:
        print('NINGUÉM GANHOU! DEU EMPATE!')
else:
    print('Você jogou uma opção INVÁLIDA!')
