# desenvolva um programa que leia o primeira termo e a razão de uma PA, mostrando os 10 primeiros termos dessa progressão.

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao

for c in range(primeiro, decimo + razao, razao):
    print(c, end='-> ')
print('Acabou!')
