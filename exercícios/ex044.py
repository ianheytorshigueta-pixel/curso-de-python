"""Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros"""

nome = ' LOJAS IAN '
print(f'{nome:=^30}')
precoi = float(input('Preço das compras: R$'))
opcao = int(input('FORMAS DE PAGAMENTO'
                  '\n[ 1 ] à vista dinheiro/cheque'
                  '\n[ 2 ] à vista no cartão'
                  '\n[ 3 ] 2x no cartão'
                  '\n[ 4 ] 3x no cartão'
                  '\nQual é a opção: '))
if opcao == 1:
    precof = precoi - (precoi*0.10)
    print(f'Sua compra de R${precoi} vai custar R${precof:.2f}')
elif opcao == 2:
    precof = precoi - (precoi*0.05)
    print(f'Sua compra de R${precoi} vai custar R${precof:.2f}')
elif opcao == 3:
    print(f'Sua compra será parcelada em 2x de R${(precoi/2):.2f}')
elif opcao == 4:
    parcela = int(input('Quantas parcelas? '))
    precof = precoi + (precoi * 0.20)
    custo_p = precof/parcela
    print(f'Sua compra será parcelada em {parcela}x de R${custo_p:.2f} COM JUROS.')
    print(f'Sua compra de R${precoi} vai custar R${precof:.2f} no final.')
