"""Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual
foi o maior e o menor valor digitado e as suas respectivas posições na lista."""

valores = list()
maior = 0
menor = 0
for p in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {p}: ')))
    if p == 0:
        maior = menor = valores[p]
    else:
        if valores[p] > maior:
            maior = valores[p]
        elif valores[p] < menor:
            menor = valores[p]
print('-='*30)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for pos ,v in enumerate(valores):
    if v == maior:
        print(pos, end='... ')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for pos, v in enumerate(valores):
    if v == menor:
        print(pos, end='... ')
print()