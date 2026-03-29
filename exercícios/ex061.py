""" Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while."""

a1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
a10 = a1 + 9*r
while a1 != a10 + r:
    print(f'{a1} → ', end='')
    a1 += r
print('FIM')
