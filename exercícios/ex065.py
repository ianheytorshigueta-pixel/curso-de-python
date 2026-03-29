""""Crie um programa que leia vários números inteiros pelo teclado. No final
da execução, mostre a média entre todos os valores e qual foi o maior e o
menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não
continuar a digitar valores."""

contador = 0
somador = 0
maior = 0
menor = 0
resp = 'S'
while resp not in 'Nn':
    num = int(input('Digite um número: '))
    contador += 1
    if contador == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    somador += num
    resp = str(input('Quer continuar [S/N]? ')).strip()[0]
media = somador/contador
print(f'Você digitou {contador} números é a média foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
