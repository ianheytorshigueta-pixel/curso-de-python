"""Escreva um programa que leia um número inteiro qualquer e peça para o
usuário escolher qual será a base de conversão:
- 1 para binário
- 2 para octal
- 3 hexadecimal"""

num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:'
      '\n[ 1 ] converter pra BINÁRIO'
      '\n[ 2 ] converter pra OCTAL'
      '\n[ 3 ] converter para HEXADECIMAL')
opcao = int(input('Sua opção: '))
novo_num = num
nome = ''
if opcao < 1 or opcao > 3:
    print('Opção inválida! Tente novamente.')
else:
    if opcao == 1:
        novo_num = bin(num)[2:]
        nome = 'BINÁRIO'
    elif opcao == 2:
        novo_num = oct(num)[2:]
        nome = 'OCTAL'
    else:
        novo_num = hex(num)[2:]
        nome = 'HEXADECIMAL'
    print(f'{num} convertido para {nome} é igual a {novo_num}')
