"""Crie um programa que leia o nome completo de uma pessoa e mostre:
-> O nome com todas as letras maiúsculas
-> O nome com todas minúsculas
-> Quantas letras ao total (sem considerar espaços)
-> Quantas letra tem o primeiro nome"""


nome = str(input('Digite seu nome completo: '))
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(' ')}')
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e tem {nome.find(' ')}')
