"""Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor)."""

CORTE = 100
sumatoria = 0
promedio = 0
contador = 0

while contador < CORTE:
    numero = int(input("Ingrese un número entero positivo: "))
    sumatoria += numero
    contador += 1

print(f'El promedio de los números ingresados es: {sumatoria / contador}')

