"""Escreva um programa que pergunte o salário de um funcionário e calcule o
valor de seu aumento.

Para salários superiores a R$1.250,00, calcule um aumento de 10%.

Para os inferiores ou iguais, o aumento é de 15%."""

salario = float(input('Qual é o salário do funcionário? R$'))
reajuste = salario + salario*0.1 if salario > 1250 else salario + salario*0.15
print(f'Quem ganhava R${salario} passa a ganhar R${reajuste:.2f} agora.')
