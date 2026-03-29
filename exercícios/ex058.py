"""Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número
entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando
no final quantos palpites foram necessários para vencer."""

from random import randint
jogador = int(input('Sou seu computador...'
                    '\nAcabei de pensar em um número entre 0 e 10.'
                    '\nSerá que você consegue adivinhar qual foi?'
                    '\nQual o seu palpite? '))
computador = randint(0, 10)
acertou = False
tentativas = 1
while not acertou:
    if jogador == computador:
        acertou = True
    if jogador > computador:
        print('Menos... Tente mais uma vez.')
    else:
        print('Mais... Tente mais uma vez.')
    jogador = int(input('Qual o seu palpite? '))
    tentativas += 1
print(f'Acertou com {tentativas} tentativas. Parabéns!')
