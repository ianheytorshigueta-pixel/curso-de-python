"""Crie um programa que simule o funcionamento de um caixa eletrônico. No
início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o
programa vai informar quantas cédulas de cada valor serão entregues.

OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1."""

valor = float(input('Qual valor você quer sacar? R$'))
val_ced = 0 #valor da cédula

while True:
    tot_ced = 0
    if valor >= 50:
        val_ced = 50
    elif valor >= 20:
        val_ced = 20
    elif valor >= 10:
        val_ced = 10
    elif valor >= 1:
        val_ced = 1
    else:
        break
    while valor >= val_ced:
        tot_ced += 1
        valor -= val_ced
    print(f'Total de {tot_ced} cédulas de R${val_ced}')

