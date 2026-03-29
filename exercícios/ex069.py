"""Crie um programa que leia a idade e o sexo de várias pessoas. A cada
pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos."""

XVIIItot = 0 #pessoas com mais de 18 anos
tothomens = 0 #total de homens
XXtotmulheres = 0 #mulheres com menos de 20 anos
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade = int(input('Idade: '))
    if idade > 18:
        XVIIItot += 1
    sexo = str(input('Sexo: [M/F] '))
    if sexo.strip()[0] in 'Mm':
        tothomens += 1
    else:
        if idade < 20:
            XXtotmulheres += 1
    resp = str(input('Quer continuar? [S/N] '))
    if resp.strip()[0] in 'Nn':
        break
print(f'Total de pessoas com mais de 18 anos: {XVIIItot}')
print(f'Ao todo temos {tothomens} homen(s) cadastrado(s).')
print(f'E temos {XXtotmulheres} mulher(es) com menos de 20 anos.')
