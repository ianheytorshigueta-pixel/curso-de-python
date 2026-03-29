"""Faça um programa que leia uma frase pelo teclado e mostre

-> Quantas vezes aparece a letra A.
-> Em que posição ela aparece da primeira vez.
-> Em que posição ela aparece pela última vez."""

frase = str(input('Digite uma sentença qualquer: ')).strip().lower()
print(f'Quantidade de vezes que apareceu a letra A: {frase.count('a')}')
print(f'A primeira letra A apareceu na posição {frase.find('a') + 1}')
print(f'A letra A apareceu pela última vez na posição {frase.rfind('a') + 1}')
