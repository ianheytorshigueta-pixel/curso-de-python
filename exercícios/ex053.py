"""Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços."""

frase = str(input('Digite uma frase: ')).strip().split()
juntar_frase = ''.join(frase)
nova_frase = juntar_frase.upper()
frase_invertida = ''
for c in range(len(nova_frase)-1, -1, -1):
    frase_invertida += f'{nova_frase[c]}'
print(f'O inverso de {nova_frase} é {frase_invertida}.')
if nova_frase == frase_invertida:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
