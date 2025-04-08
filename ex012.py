# faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

while True:
    try:
        preco = float(input('Digite o preço do produto: R$ '))
        desconto = preco * 0.05
        preco_final = preco - desconto
        print(f'Desconto: R$ {desconto:.2f}')
        print(f'O preço do produto com 5% de desconto é: R$ {preco_final:.2f}')
        break  
    except ValueError:
        print('Erro: por favor, digite um número válido para o preço.\n')


