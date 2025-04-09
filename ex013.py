# faça um algoritimo que leia o salario e mostre seu novo salario, com 15% de aumento.
salario = float(input('Digite o salário: R$ '))

aumento = salario * 0.15

salario_final = salario + aumento

print(f'o salario com 15% de aumento é R$: {salario_final:.2f}')