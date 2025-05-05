# faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a idade dele, se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

atual = date.today().year

nasc = int(input('Ano de nascimento: '))
idade = atual - nasc

print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print(f'vc ainda não tem 18 anos, ainda faltam {18 - idade} anos para o alistamento.')
elif idade > 18:
    ano = idade - 18
    print(f'Você já deveria ter se alistado há {idade - 18} anos.')
    
