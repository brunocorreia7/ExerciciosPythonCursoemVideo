#faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))

area = largura * altura

tinta = area / 2
print(f'A área da parede é {area:.2f} m² e você precisará de {tinta:.2f} litros de tinta para pintá-la.')