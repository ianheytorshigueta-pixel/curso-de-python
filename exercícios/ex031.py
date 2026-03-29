"""Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule
o preço passagem, cobrando R$0,50 por Km para viagens de até 200km e R$0,45 para
viagens mais longas."""

distancia = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de de {distancia:.1f}Km.')
preco = distancia*0.50 if distancia <= 200 else distancia*0.45
print(f'E o preço de sua passagem será de R${preco:.2f}')
