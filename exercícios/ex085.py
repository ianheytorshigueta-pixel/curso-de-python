"""Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma
lista única que mantenha separados os valores pares e ímpares. No final,
mostre os valores pares e ímpares em ordem crescente."""

par_impar = [[],[]]
for c in range(1, 8):
    numero = int(input(f'Digite o {c}° valor: '))
    if numero % 2 == 0:
        par_impar[0].append(numero)
    else:
        par_impar[1].append(numero)
par_impar[0].sort()
par_impar[1].sort()
print('-='*30)
print(f'Os valores pares digitados foram: {par_impar[0]}')
print(f'Os valores ímpares digitados foram: {sorted(par_impar[1])}')
