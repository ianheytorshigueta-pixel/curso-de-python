"""Faça um algoritmo que leia o salário de um funcionário e mostre
seu novo salário com 15% de aumento."""

salario = float(input("Qual o salário do funcionário? R$"))
aumento = salario*0.15
novo_salario = salario + aumento
print(f"Um funcionário que ganhava R${salario:.2f}, com 15% de aumento, passa "
      f"a receber R${novo_salario:.2f}")
