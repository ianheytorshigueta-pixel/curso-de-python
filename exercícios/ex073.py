"""Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de
Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense."""

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória',
        'Coritiba', 'Avaí', 'Ponte Petra', 'Atlético-GO')
print('-='*15)
print(f'times do Brasileirão: {times}')
print('-='*15)
print(f'Os 5 primeiros são: {times}')
print('-='*15)
print(f'O 4 últimos são: {times[-5:-1]}')
print('-='*15)
print(f'Times em ordem alfabética: {sorted(times)}')