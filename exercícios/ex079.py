""" Crie um programa onde o usuário possa digitar vários valores
numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro,
ele não será adicionado. No final, serão exibidos todos os valores únicos
digitados, em ordem crescente."""

valores = list()
while True:
    v = int(input('Digite um valor: '))
    if v not in valores:
        valores.append(v)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar.')
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp[0] in 'N':
        break
print('-='*30)
valores.sort()
print(f'Você adicionou os valores {valores}')
