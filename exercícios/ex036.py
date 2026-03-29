"""Escreva um programa para aprovar um empréstimo bancário para a compra de uma\
casa. O programa vai perguntar o valor da casa, o salário do comprador e em
quantos anos ele vai pagar.

Calcule o valor da prestação mensal. Sabendo que ela não pode exceder 30% do
salário ou então o empréstimo será negado."""

casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
parcela = casa/(anos*12)
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos a prestação será de'
      f' R${parcela:.2f}')
if parcela > (salario*0.3):
    print('EMPRÉSTIMO NEGADO!')
else:
    print('EMPRÉSTIMO ACEITO!')
