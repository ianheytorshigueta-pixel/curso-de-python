"""Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de
zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por
extenso."""

numero = int(input('Digite um número entre 0 e 20: '))
while True:
    if 0 <= numero <= 20:
        extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
                    'seis', 'sete', 'oito', 'nove', 'dez',
                    'onze', 'doze', 'treze', 'quatorze', 'quinze',
                    'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
        break
    else:
        numero = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'Você digitou o número {extenso[numero]}')
