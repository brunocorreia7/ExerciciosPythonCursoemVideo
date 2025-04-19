# faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.
# Ex: Digite um número: 1834
# unidade: 4 dezena: 3 centena: 8 milhar: 1

num = input('Digite um número de 0 a 9999: ').zfill(4)

print(f'Analisando o número {num}')
print(f'Unidade: {num[3]}')
print(f'Dezena: {num[2]}')
print(f'Centena: {num[1]}')

print(f'Milhar: {num[0]}')



