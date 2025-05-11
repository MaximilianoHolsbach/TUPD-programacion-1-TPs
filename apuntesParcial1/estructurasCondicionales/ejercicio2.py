"""
1. Solicita una letra al usuario. 
2. Si es una vocal (a, e, i, o, u, en mayúscula o minúscula), imprime: "La letra 
ingresada es una vocal". 
3. En otro caso, imprime: "La letra ingresada no es una vocal". 

_____________________________________________________

¿Cómo manejarías vocales acentuadas (á, é)? 
- Para manejar vocales acentuadas, se puede agregar una lista de vocales acentuadas a la constante VOCALES y luego verificar si la letra ingresada está en esa lista.

¿Qué estructura usarías para simplificar las comparaciones?
- Para simplificar las comparaciones, se puede usar una cadena de texto que contenga todas las vocales y vocales acentuadas, y luego verificar si la letra ingresada está en esa cadena.
"""
# Definición de constantes
VOCALES = "aeiouáéíóú"

# Ingreso de datos y asignación de variables
cadena = input("Introduce una vocal: ").lower()

if cadena in VOCALES:
    print(f"Ingresaste la vocal {cadena}.")
else:
    print(f"{cadena} no es una vocal.")

