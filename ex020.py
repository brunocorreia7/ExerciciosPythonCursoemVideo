# o mesmo professor do desafio anterior quer sortear a ordem da apresentação de trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

lista = []

for i in range(1, 5):
    aluno = input(f"Digite o nome do {i}º aluno: ")
    lista.append(aluno)

random.shuffle(lista)

print('A ordem de apresentação será: ')
print(lista)

