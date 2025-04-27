# desenvolva um programa que calcule a distancia de uma viagem em km. Calcule o preco da passagem, cobrando R$0,50 por km para viagens de ate 200km e R$0,45 para viagens mais longas.

distancia = float(input('Qual a distancia da sua viagem? '))
print(f'você vai começar uma viagem de {distancia}km.')
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print(f'O preço da sua passagem será de R${preco:.2f}')