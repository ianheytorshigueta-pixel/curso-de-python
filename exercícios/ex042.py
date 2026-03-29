"""Refaça o exercício 35 dos triângulos, acrescentando o recurso de mostrar
que tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguias
- Escaleno: todos os lados diferentes"""

s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    triangulo = ''
    if s1 == s2 == s3:
        triangulo = 'EQUILÁTERO'
    elif (s1 == s2 and s2 != s3) or (s1 == s3 and s3 != s2) or (s2 == s3 and s2 != s1):
        triangulo = 'ISÓSCELES'
    else:
        triangulo = 'ESCALENO'
    print(f'Os segmentos acima PODEM FORMAR um triângulo {triangulo}!')
else:
    print('Os segmentos NÃO PODEM FORMAR triângulo!')
