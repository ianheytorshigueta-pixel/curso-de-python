"""Crie um programa que leia o nome e o preço de vários produtos. O programa
deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. """

nome_da_loja = 'LOJA SUPER BARATÃO'
print('='*28)
print(f'{nome_da_loja:^28}')
print('='*28)
tot_compra = 0
tot_maisde_mil = 0
menor = 0
cont = 0
nome = ''
while True:
    cont += 1
    nome_produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    if cont == 1:
        menor = preco
        nome = nome_produto
    else:
        if preco < menor:
            menor = preco
            nome = nome_produto
    tot_compra += preco
    if preco > 1000:
        tot_maisde_mil += 1
    resp = str(input('Quer continuar? [S/N] ')).strip()
    if resp[0] in 'Nn':
        break
print(f'{' Fim do Programa ':-^37}')
print(f'O total da compra foi de R${tot_compra:.2f}')
print(f'Temos {tot_maisde_mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome} que custa R${menor:.2f}')
