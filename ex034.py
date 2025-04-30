# escreva um programa que escreva o salario de um funcionario e calcule o valor do seu aumento. 
# para salarios superiores a 1250,00 o aumento será de 10% e para inferiores, de 15%

salario = float(input('Digite o salário do funcionário: R$ '))
if salario > 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
    
print(f'O novo salário do funcionário é R$ {novo:.2f}')
  
