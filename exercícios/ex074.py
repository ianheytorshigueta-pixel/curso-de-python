"""Crie um programa que vai gerar cinco números aleatórios e
colocar em uma tupla. Depois disso, mostre a listagem de números
gerados e também indique o menor e o maior valor que estão na tupla."""

from random import randint
numero = list()
valores = ()
for c in range(0, 5):
    numero += [randint(0, 9)]
    valores = tuple(numero)
print('Os valores sorteados foram: ', end='')
for v in valores:
    print(v, end=' ')
print(f'\nO maior valor sorteado foi {max(valores)}')
print(f'O menor valor sorteado foi {min(valores)}')
