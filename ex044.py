# elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e a condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# em ate 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

preco = float(input('Digite o preço do produto: '))
print('''Formas de pagamento:

[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opcao = int(input('Qual é a opção '))
if opcao ==1:
    preco = preco - (preco * 10 / 100)
    print(f'O valor a ser pago é R$ {preco:.2f}')
elif opcao == 2:
    preco = preco - (preco * 5 / 100)
    print(f'O valor a ser pago é R$ {preco:.2f}')
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R$ {parcela:.2f} sem juros')
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    parcelas = int(input('Quantas parcelas? '))
    parcela = total / parcelas
    print(f'Sua compra será parcelada em {parcelas}x de R$ {parcela:.2f} com juros')
else:
    print('Opção inválida. Tente novamente.')
    

      
      
      
      
      


