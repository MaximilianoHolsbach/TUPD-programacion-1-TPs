"""Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0."""
corte = True
sumatoria = 0
while corte:
    numero = int(input("Ingrese un número entero positivo: "))
    sumatoria += numero
    corte = numero != 0 # Se detiene el ciclo cuando el usuario ingresa 0
print(f'La sumatoria de los números ingresados es: {sumatoria}')