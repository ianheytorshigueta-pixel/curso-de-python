"""Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos dólares ela pode comprar.

Considere:
US$1,00 = R$3,27"""

reais = float(input("Quanto dinheiro você tem na carteira? R$"))
dolares = reais/3.27
print(f"Com R${reais:.2f} você poderá comprar US${dolares:.2f}.")
