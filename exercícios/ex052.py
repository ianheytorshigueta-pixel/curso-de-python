"""Faça um programa que leia um número inteiro e diga se ele é ou não um
número primo."""

contador = 0
n = int(input('Digite um número: '))
for c in range(1, n+1):
    if n % c == 0:
        contador += 1
        print('\033[1;33m', end='')
    else:
        print('\033[1;31m', end='')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {n} foi divisível {contador} vezes.')
if contador > 2 or contador == 1:
    print('E por isso ele NÃO É PRIMO.')
else:
    print('E por isso ele É PRIMO.')
