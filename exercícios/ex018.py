"""Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
cosseno e tangente desse ângulo"""

from math import radians, sin, cos, tan
ang = float(input("Digite o ângulo que você deseja: "))
rad = radians(ang)
seno = sin(rad)
print(f"O ângulo de {ang} tem o SENO de {seno:.2f}")
cosseno = cos(rad)
print(f"O ângulo de {ang} tem COSSENO de {cosseno:.2f}")
tangente = tan(rad)
print(f"O ângulo de {ang} tem TANGENTE de {tangente:.2f}")
