# refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

print('=-'*20)
print('Analisador de triângulos')
print('=-'*20)

for c in range(1,4):
    r = float(input(f'digite o comprimento da reta {c}: '))
    if c == 1:
        r1 = r
    elif c == 2:
        r2 = r
    else:
        r3 = r
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('os seguimentos acima podem formar um triângulo')
    
    if r1 == r2 and r2 == r3:
        print('triângulo EQUILÁTERO')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('triângulo ISÓSCELES')
    else:
        print('triângulo ESCALENO')
else:
    print('os retasseguimentos acima não podem formar um triângulo')
