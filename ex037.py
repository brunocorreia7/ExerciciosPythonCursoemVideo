# escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual será a base de conversão. 1 para binário, 2 para octal e 3 para hexadecimal. Mostre o resultado da conversão na tela.

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] para binário
[ 2 ] para octal
[ 3 ] para hexadecimal''')

opção = int(input('Sua opção: '))
if opção == 1:
    print(f'{num} em binário é {bin(num)[2:]}')
elif opção == 2: 
    print(f'{num} em octal é {oct(num)[2:]}')
elif opção == 3:
    print(f'{num} em hexadecimal é {hex(num)[2:]}')
else:
    print('Opção inválida! Tente novamente.')
