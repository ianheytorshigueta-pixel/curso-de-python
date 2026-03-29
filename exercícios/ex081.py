"""Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""

valores = list()
cont =+ 0
while True:
    valores.append(int(input('Digite um valor: ')))
    cont += 1
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp[0] in 'N':
        break
print('-='*30)
print(f'Você digitou {cont} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print(f'O valor 5 faz parte da lista.')
