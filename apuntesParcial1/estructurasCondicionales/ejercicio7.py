"""
• ¿Cómo manejarías frases que terminan con espacios? 
- Se podría utilizar el método `strip()` para eliminar los espacios en blanco al principio y al final de la cadena antes de verificar si termina con un punto.

• ¿Qué otros caracteres de puntuación podrías considerar?
- Se podrían considerar otros caracteres de puntuación como signos de interrogación (?), signos de exclamación (!), comas (,), entre otros, dependiendo del contexto y la necesidad de la validación.
"""

# Definición de constantes
CARACTER = "."

# Ingreso de datos y asignación de variables
cadena = input("Introduce una frase: ").lower()

# Ejecución de la estructura condicional
if cadena[-1] == CARACTER:
    print("Cadena terminada en punto.")
else:
    cadena = cadena + CARACTER
    print(f"Cadena modificada: \n{cadena}")

