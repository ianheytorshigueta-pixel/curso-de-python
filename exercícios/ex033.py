"""Faça um programa que leia três números e mostre qual é o maior e qual é o
menor."""

n_1 = int(input('Primeiro Valor: '))
n_2 = int(input('Segundo Valor: '))
n_3 = int(input('Terceiro valor: '))
menor = n_1
if n_2 < menor:
    menor = n_2
if n_3 < menor:
    menor = n_3
print(f'O menor valor digitado foi {menor}')
maior = n_1
if n_2 > n_1:
    maior = n_2
if n_3 > maior:
    maior = n_3
print(f'O maior valro digitado foi {maior}')
