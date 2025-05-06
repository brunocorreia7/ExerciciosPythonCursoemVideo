# crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO  
# - Média 7.0 ou superior: APROVADO
notas = []

for c in range(1, 3):
    n = float(input(f'Digite a {c}° nota: '))
    notas.append(n)

nota1, nota2 = notas
media = (nota1 + nota2) / 2
print(f'A média entre {nota1} e {nota2} é {media:.1f}.')
if media < 5.0:
    print('REPROVADO')
elif 5.0 <= media < 7.0:
    print('RECUPERAÇÃO')
elif media >= 7.0:
    print('APROVADO')
