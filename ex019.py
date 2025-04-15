# um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random

alunos = []

for i in range(1, 5):
    aluno = input(f"Digite o nome do {i}º aluno: ")
    alunos.append(aluno)

escolhido = random.choice(alunos)

print(f"O aluno escolhido foi: {escolhido}")
