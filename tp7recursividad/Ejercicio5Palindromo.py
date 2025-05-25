"""
Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed()
Una palabra es un palíndromo si se lee igual de izquierda a derecha que de derecha a izquierda.
Ejemplos:
- anilina -> True
- oso -> True
- osoo -> False
"""

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    else:
        return palabra[0] == palabra[-1] and es_palindromo(palabra[1:-1])
    
# Solicitar al usuario una palabra
palabra = input("Introduce una palabra: ")

# Verificar si la palabra es un palíndromo utilizando la función recursiva

print(f"La palabra '{palabra}' es un palíndromo: {es_palindromo(palabra)}")

