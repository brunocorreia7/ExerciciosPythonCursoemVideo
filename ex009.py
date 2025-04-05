# faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada.

def mostrar_tabuada(num):
    for c in range(1, 11):
        print(f'{num} X {c} = {num * c}')


num = int(input('Digite um número para ver sua tabuada: '))
mostrar_tabuada(num)
