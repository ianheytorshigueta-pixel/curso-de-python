"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome
do homem mais velho e quantas mulheres têm menos de 20 anos."""

somador = 0
m_idade_h = 0
n_homem = ''
s_mulher = 0
for c in range(1, 5, 1):
    indice = f' {c}ª PESSOA '
    print(f'{indice:-^22}')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    somador += idade
    sexo = str(input('Sexo [M/F]: '))
    if sexo[0] in 'Mm' and idade > m_idade_h:
        m_idade_h = idade
        n_homem = nome
    if sexo[0] in 'Ff' and idade < 20:
        s_mulher += 1
media = somador/4
print(f'A média de idade do grupo é de {media:.1f}')
print(f'O homem mais velho tel {m_idade_h} anos e se chama {n_homem}.')
print(f'Ao todo são {s_mulher} mulheres com menos de 20 anos')
