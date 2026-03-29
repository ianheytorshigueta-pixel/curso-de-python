"""Faça um programa que jogue par ou ímpar com o computador. O jogo só será
interrompido quando o jogador perder, mostrando o total de vitórias consecutivas
que ele conquistou no final do jogo."""

from random import randint
print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)
vitorias = 0
while True:
    num_player = int(input('Diga um valor: '))
    choice = str(input('Par ou Ímpar? [P/I] ')).strip()[0]
    num_machine = randint(1, 10)
    soma = num_player + num_machine
    if soma % 2 == 0:
        texto = 'DEU PAR'
    else:
        texto = 'DEU ÍMPAR'
    print('-'*30)
    print(f'Você jogou {num_player} e o computador {num_machine}. '
          f'Total de {soma} {texto}')
    print('-'*30)
    if (choice in 'Pp' and soma % 2 == 0) or (choice in 'Ii' and soma % 2 != 0):
        print('Você VENCEU!'
              '\nVamos jogar novamente...')
        vitorias += 1
    else:
        print('Você PERDEU!')
        break
print(f'GAME OVER! Você venceu {vitorias} vez(es).')
