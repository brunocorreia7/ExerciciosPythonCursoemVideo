# faça um programa que leia o nome completo de uma pessoa. Mostrando em seguida o primeiro e o último nome separadamente.
# exemplo Ana Maria de sousa
# primeiro = Ana    
# último = Sousa

n = str(input('Digite o nome completo: ')).strip()
nome = n.split()
print(f'Primeiro nome: {nome[0]}')
print(f'Último nome: {nome[-1]}')







