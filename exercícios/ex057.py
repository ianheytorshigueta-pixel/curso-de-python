"""Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, p
peça a digitação novamente até ter um valor correto."""

sexo = str(input('Informe o seu sexo: [M/F] ')).strip()[0]
while sexo not in 'FfMm':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip()[0]
print(f'Sexo {sexo.upper()} registrado com sucesso!')
