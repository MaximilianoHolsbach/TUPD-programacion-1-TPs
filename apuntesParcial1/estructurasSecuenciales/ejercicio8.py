"""
Preguntas de reflexión:
• ¿Qué técnicas de manipulación de strings estás usando?
- Estoy usando la función len() para contar los caracteres, el método replace() para eliminar los espacios, y el metodo de slicing para obtener los primeros tres caracteres.
• ¿Cómo podrías extender este ejercicio para apellidos?
- Solicitamos al usuario lo agregue y aplicamos los mismos métodos.
"""

# Definicion de variables
nombre = input("Ingrese su nombre completo: ")

# Definicion de operaciones

contarCaracteres = len(nombre.replace(" ",""))

# Definicion de salida

print(f"La cantidad de caracteres en su nombre es: {contarCaracteres}")

print(f"Los tres primeros caracteres son: {nombre[0:3]}")

