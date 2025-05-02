# escreva um programa para aprovar emprestimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o seu salário? R$ '))   

anos = int(input('Em quantos anos você vai pagar? '))
prestacao = casa / (anos * 12)
porcentagem = salario * 0.3
print(f'A prestação mensal será de R$ {prestacao:.2f}')
print(f'30% do seu salário é R$ {porcentagem:.2f}')
if prestacao <= porcentagem:
    print('Empréstimo aprovado!')
else:
    print('Empréstimo negado!')