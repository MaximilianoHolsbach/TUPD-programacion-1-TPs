"""
Objetivo: Calcular el área y el perímetro a partir de medidas dadas por el 
usuario
 Instrucciones: 
1. Pedir al usuario que ingrese el ancho y el alto de un rectángulo. 
2. Calcular el área usando la fórmula: ancho * alto. 
3. Calcular el perímetro con la fórmula: (ancho * 2) + (alto * 2). 
4. Mostrar ambos resultados en pantalla.
"""

# Ingreso de datos

ancho = int(input("Ingrese el ancho del rectángulo: "))
alto = int(input("Ingrese el alto del rectángulo: "))

# Calculo del área
area = ancho * alto
perimetro = 2 * (ancho + alto)

# Salida de datos

print(f"El aréa del rectángulo es: {area}")
print(f"El perímetro del rectángulo es: {perimetro}")

