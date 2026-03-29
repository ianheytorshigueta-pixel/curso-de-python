"""Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores
pares e os valores ímpares digitados, respectivamente. Ao final, mostre o
conteúdo das três listas geradas."""

valores = list()
par = list()
impar = list()
while True:
    v = int(input('Digite um número: '))
    valores.append(v)
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    if resp[0] in 'N':
        break
for n in valores:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
