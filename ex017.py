# faça um programa que leia o comprimento de um cateto oposto e o comprimento de um cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.

import math

cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

hipotenusa = math.sqrt(cateto_oposto**2 + cateto_adjacente**2)

print(f"O comprimento da hipotenusa é: {hipotenusa:.2f}")

