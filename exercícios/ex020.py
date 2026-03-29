"""O mesmo professor do desafio anterior quer sortear a ordem de apresentação detrabalhos
dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada"""

from random import sample
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
alunos = [a1, a2, a3, a4]
sorteio = sample(alunos, k=len(alunos))
print(f"A ordem de apresentação do trabalho será \n{sorteio}")
