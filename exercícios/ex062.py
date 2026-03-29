""" Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar
mais alguns termos. O programa encerrará quando ele disser que quer mostrar
0 termos."""

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
total = 0
a_mais = 10
while a_mais != 0:
    for contador in range(1, a_mais + 1, 1):
        print(f'{primeiro} → ', end='')
        primeiro += razao
        total += 1
    print('PAUSA')
    a_mais = int(input('Quantos termos você quer mostrar a mais: '))
print(f'Progressão finalizada com {cont} termos mostrados.')
