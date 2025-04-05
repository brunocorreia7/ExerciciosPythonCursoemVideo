# algoritimo que le um numero e mostre o seu sobro, o seu triplo e a raiz quadrada
import math
n = int(input('digite um numero: '))
dobro = n * 2
triplo = n * 3
raiz = math.sqrt(n) 

print(f'o dobro de {n} é {dobro}, o triplo é {triplo} e a raiz quadrada é {raiz:.0f}')