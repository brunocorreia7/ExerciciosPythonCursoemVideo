# escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e 0,15 pir km rodado.

dias = float(input('quantos dias alugado: '))
km = float(input('quantos km rodados: '))

pago = (dias * 60) + (km * 0.15)

print(f'o total a pagar é de R${pago:.2f}')
