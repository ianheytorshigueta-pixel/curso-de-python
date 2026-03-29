"""Escreva um programa que leia dois números inteiros e compare-os, mostrando
na tela uma mensagem.

- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais"""

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
maior = ''
if n1 != n2:
    if n1 > n2:
        maior = 'PRIMEIRO'
    else:
        maior = 'SEGUNDO'
    print(f'O {maior} valor é maior')
else:
    print('Os dois valores são IGUAIS.')
