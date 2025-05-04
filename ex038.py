# escreva um programa que leia dois numeros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior 
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

numeros = []
for c in range(1, 3):
    n = int(input(f'Digite o {c}° número: '))
    numeros.append(n)

n1, n2 = numeros

if n1 > n2:
    print(f'O primeiro valor é maior: {n1}')
elif n2 > n1:
    print(f'O segundo valor é maior: {n2}')
else:
    print('Não existe valor maior, os dois são iguais')
        
        
