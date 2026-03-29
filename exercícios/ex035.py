"""Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
se elas podem ou não formar um triângulo."""

print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
valor = False
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    valor = True
if valor:
    print('Os segmentos acima PODEM FORMAR triângulo.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo.')
