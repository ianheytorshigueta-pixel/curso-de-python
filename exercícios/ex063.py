"""Escreva um programa que leia um número N inteiro qualquer e mostre na tela
os N primeiros elementos de uma Sequência de Fibonacci.

Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8"""

print('-'*25)
print('Sequência de Fibbonacci')
print('-'*25)
limite = int(input('Quantos termos você quer mostrar? '))
cont = 0
t1 = 0
t2 = 1
print(f'{t1} → {t2} → ', end='')
while cont != limite:
    t3 = t1 + t2
    print(f'{t3} → ', end='')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
