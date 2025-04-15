"""
escribir un programa que tome la lista
numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

"""

from statistics import median, mean
import random
sesgo = ''
numerosAleatorios = [random.randint(1, 100) for i in range(50)]

mediana = median(numerosAleatorios)
media = mean(numerosAleatorios)

if media > mediana:
    sesgo = 'positivo'
elif media < mediana:
    sesgo = 'negativo'
else:
    sesgo = 'neutro'  

print(f'El sesgo en la lista de números aleatorios es: {sesgo}')

