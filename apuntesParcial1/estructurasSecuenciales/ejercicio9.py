"""
• ¿Qué ocurre si redondeás a más decimales?
- Si redondeo a más decimales, el resultado se ajustará a la cantidad de decimales especificado.
• ¿Cuándo conviene usar math.pow()?
- Conviene usar math.pow() cuando se necesita calcular potencias con exponentes no enteros o cuando se requiere mayor precisión en el cálculo de potencias.

"""
import math
# Definicion de variables

a = 7.5
b = 3.2

# Definicion de operaciones
suma = a + b
division = (a / b).__round__(2)
potencia = math.pow(a, b)

# Definicion de salida

print(f"La suma de {a} y {b} es: {suma}")
print(f"La division de {a} entre {b} es: {division}")
print(f"La potencia de {a} elevado a {b} es: {potencia}")

