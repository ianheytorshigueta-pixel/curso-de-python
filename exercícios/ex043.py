"""Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule o
seu IMC e mostre seu status, de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida"""

peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso/(altura**2)
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print('Você está ABAIXO DO PESO! Precisa comer mais.')
elif 18.5 <= imc < 25:
    print('Parabéns! Você alcançou o PESO IDEAL!')
elif 25 <= imc < 30:
    print('Maneire um pouco na comida. Você está em SOBREPESO!')
elif 30 <= imc < 40:
    print('É melhor tomar cuidado... OBESIDADE é coisa séria!')
else:
    print('PERIGO!!! OBESIDADE MÓRBIDA! VOCÊ PODE MORRER!')
