# desenvolva um programa que leia o comprimento de 3 retas e diga ao usuario se elas podem ou não formar um triangulo.
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
    print('As retas podem formar um triângulo')
else:
    print('As retas não podem formar um triângulo')
