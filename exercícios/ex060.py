""" Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120"""

n = int(input('''Digite um número para 
calcular seu Fatorial: '''))
fatorial = 1
print(f'Calculando {n}! = ', end='')
while n != 0:
    print(f'{n} ', end='')
    print('x' if n > 1 else '=', end=' ')
    fatorial *= n
    n -= 1
print(fatorial)
