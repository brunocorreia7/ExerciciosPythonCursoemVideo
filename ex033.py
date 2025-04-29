# faça um programa que leia 3 numeros e mostre qual é o maior e qual é o menor.

for i in range(1,4):
    n = int(input(f'Digite o {i}° número: '))
    
    if i == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
            
print(f'O maior número é {maior} e o menor é {menor}.')


            
