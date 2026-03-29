"""Faça um programa que leia o nome completo de uma pessoa, mostrando em
seguida o primeiro e o último nome separadamente."""

nome = str(input('Digite seu nome completo: ')).strip().title()
separa = nome.split()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {separa[0]}'
      f'\nSeu último nome é {separa[-1]}')
