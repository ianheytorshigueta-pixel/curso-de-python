"""Crie um programa que leie um número inteiro e mostre na tela se ele é PAR
ou ÍMPAR."""

num = int(input('\033[35mDiga-me um número qualquer: \033[37m'))
if num % 2 == 0:
    print(f'O número {num} é \033[34mPAR!')
else:
    print(f'O número {num} é \033[34mÍMPAR!')
