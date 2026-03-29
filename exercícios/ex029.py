"""Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar
80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar
R$7,00 por cada km acima do limite."""

velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('\033[31mMULTADO! Você excedeu o limite permitido que é de 80km/h'
          f'\nVocê deve pagar uma multa de \033[33mR${multa:.2f}!')
print('\033[32mTenha um bom dia! Dirija com segurança!\033[33m')
