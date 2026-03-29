"""Desenvolva um programa que leia o primeiro termo de uma PA. No final, mostre
os 10 primeiro termos dessa progressão."""

print('='*50)
print(f'{'PROGRESSÃO GEOMÉTRICA':^50}')
print('='*50)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = a1 + (10-1)*r
for c in range(a1, decimo + r, r):
    print(f'{c} →', end=' ')
print('Acabou')
