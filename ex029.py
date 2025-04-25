# escreva um programa que leia a velocidade de um carro. se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado. a multa vai custar r$ 7,00 por cada km acima do limite.

velocidade = float(input('Qual é a velocidade do carro? '))

if velocidade > 80:
    print('MULTADO! Você excedeu o limite de velocidade de 80 km/h.')
    
    multa = (velocidade - 80) * 7
    
    print(f'A sua multa é de R$ {multa:.2f}')

else:
    print('Tudo certo! Você está dentro do limite de velocidade.')
