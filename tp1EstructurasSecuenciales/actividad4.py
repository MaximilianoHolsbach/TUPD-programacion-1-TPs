"""
4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
su perímetro.
"""
import math
radio = float(input("Ingrese el radio del circulo: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio
print(f"El area del circulo es: {area}, y el perimetro es: {perimetro}")