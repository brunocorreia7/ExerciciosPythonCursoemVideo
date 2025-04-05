# programa que leia quanto de dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.   
# Considere 1 dolar = 5,67 reais

def conversor_real_dolar(real):
    return real / 5.67

real = float(input('Digite quanto de dinheiro você tem na carteira: R$ '))
dolar = conversor_real_dolar(real)

print(f'Com R$ {real:.2f} você pode comprar US$ {dolar:.2f}')




