"""Faça um programa que leia a largura e altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta, pinta uma área de 2m²."""

largura = float(input("Qual a largura da parede?: "))
altura = float(input("Qual a altura da parede?: "))
area = largura*altura
litros_de_tinta = area/2
print(f"Sua parede tem dimensão de {largura}x{altura} e sua área é de {area}m²")
print(f"Para pinta essa parede, você precisará de {litros_de_tinta}l de tinta")
