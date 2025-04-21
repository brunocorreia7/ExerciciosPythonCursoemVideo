# crie um programa que leia o nome de uma pessoa e diga se ela tem "silva" no nome

nome = str(input('Digite o nome de uma pessoa: ')).strip().lower()
print(f'Seu nome tem "Silva"? {"silva" in nome}')
