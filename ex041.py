# a confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - até 9 anos: MIRIM
# - até 14 anos: INFANTIL
# - até 19 anos: JÚNIOR
# - até 20 anos: SÊNIOR
# - acima: MASTER

from datetime import date

atual = date.today().year

nascimento = int(input('Ano de nascimento: '))

idade = atual - nascimento
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:   
    print('Classificação: JÚNIOR')
elif idade <= 20:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
