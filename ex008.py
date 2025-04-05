# faça um programa que leia um valor em metros, e exiba convertido e centimentros e em milmetros.

medida = float(input('uma distancia em metros: '))
cm = medida * 100
mm = medida * 1000

print(f'a medida de {medida}m corresponde a {cm:.0f}cm \ne {mm:.0f}mm')