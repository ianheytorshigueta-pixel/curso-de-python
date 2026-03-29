"""Crie um programa que leia o ano de nascimento de sete pessoas. No final,
mostre quantas pessoas ainda não atingiram a maioridade e quantos já são
maiores."""

from datetime import date
maior_idade = 0
menor_idade = 0
for c in range(1, 8, 1):
    nasc = int(input(f'Em que ano a {c}° pessoa nasceu? '))
    idade = date.today().year - nasc
    if idade >= 18:
        maior_idade += 1
    else:
        menor_idade += 1
print(f'Ao todo tivemos {maior_idade} pessoas maiores de idade.')
print(f'E também tivemos {menor_idade} pessoas menores de idade.')
