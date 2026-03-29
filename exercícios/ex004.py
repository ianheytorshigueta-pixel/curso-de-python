"""Faça um programa que leia algo
pelo teclado e mostre na tela o seu
tipo primitivo e todas as
informações possíveis sobre ele"""

algo = input("Digite algo: ")
print(f"O tipo primitivo desse valor é {type(algo)}"
      f"\nSó tem espaços? {algo.isspace()}"
      f"\nÉ um número? {algo.isnumeric()}"
      f"\nÉ alfabético? {algo.isalpha()}"
      f"\nÉ alfanumérico? {algo.isalnum()}"
      f"\nEstá em maiúsculas? {algo.isupper()}"
      f"\nEstá em minúsculas? {algo.islower()}"
      f"\nEstá capitalizada? {algo.istitle()}")
