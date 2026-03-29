"""Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""

dado = list()
cadastros = list()
cont = 0
maior = menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if cont == 0:
        maior = menor = dado[1]
    else:
        if dado[1] >= maior:
            maior = dado[1]
        if dado[1] <= menor:
            menor = dado[1]
    cadastros.append(dado[:])
    dado.clear()
    cont += 1
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp[0] in 'N':
        break
print('-='*30)
print(f'Ao todo, você cadastros {cont} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for c in cadastros:
    if c[1] == maior:
        print(f'[{c[0]}] ', end='')
print(f'\nO menor peso foi de {menor}Kg. Peso de ', end='')
for c in cadastros:
    if c[1] == menor:
        print(f'[{c[0]}] ', end='')
