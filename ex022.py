# crie um programa que leia o nome completo de uma pessoa e mostre: o nome com todas as letras maiusculas e minusculas. quantas letras ao todo (sem considerar espaços).
# quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()

print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')

print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras')

print(f'Seu primeiro nome é {nome.split()[0]} e ele tem {len(nome.split()[0])} letras')
