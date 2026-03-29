"""Desenvolva um programa que leia seis números inteiros e mostre a soma
somente daqueles que forem pares. Se o valor digitado foi ímpar, desconsidere-o."""

somador = 0
cont = 0
for c in range(1, 7, 1):
    n = int(input(f'Digite o {c} valor número: '))
    if n % 2 == 0:
        somador += n
        cont += 1
print(f'Você informou {cont} números pares e a soam entre eles é {somador}.')
