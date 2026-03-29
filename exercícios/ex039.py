"""Faça um programa que leia o ano de nascimento de um jovem e informe, de
acordo com a sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""

from datetime import date
nasc = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} em {ano_atual}.')
if idade != 18:
    alistamento = ['', 0]
    if idade < 18:
        print(f'Ainda faltam {18-idade} ano(s) para o alistamento.')
        alistamento = ['será', ano_atual + (18-idade)]
    else:
        print(f'Você já deveria ter se alistado há {idade-18} ano(s).')
        alistamento = ['foi', ano_atual - (idade-18)]
    print(f'Seu alistamento {alistamento[0]} em {alistamento[1]}.')
else:
    print('Você tem que se alistar IMEDIATAMENTE!')
