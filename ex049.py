# refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print(f'{num} X {c} = {num * c}')

