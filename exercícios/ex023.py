"""Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos
digitos separados.

Ex:
Digite um número: 1834
Unidade: 4
Dezena: 3
Centena: 8
Milhar: 1"""

numero = int(input('Digite um número entre 0 e 9999: '))
unidade = numero % 10
print(f'Unidade: {unidade}')
dezena = numero // 10 % 10
print(f'Dezena: {dezena}')
centena = numero // 100 % 10
print(f'Centena: {centena}')
milhar = numero // 1000 % 10
print(f'Milhar: {milhar}')
