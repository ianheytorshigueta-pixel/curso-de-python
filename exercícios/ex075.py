"""Desenvolva um programa que leia quatro valores pelo teclado e
guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares."""

valores = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')))
print(f'Você digitou os valores {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vez(es)')
if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3) + 1}ª posição')
else:
    print(f'O valor 3 não apareceu nenhum vez')
tot_pares = 0
print(f'Os valores pares digitados foram: ', end='')
for v in valores:
    if v % 2 == 0:
        print(v, end=' ')
