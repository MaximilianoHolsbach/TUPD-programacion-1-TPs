"""
Obtener la suma total de los nuemros obtenidos de una lista de nuemros
Lo planteamos con un enfoque recursivo.
1. Generamos una funcion.
2. Degfinimos el caso base. 
3. Generamos un consdicional para validad el caso base.

"""

# Definimos la función sumaRecursiva que toma una lista de números como argumento.

def sumaRecursiva(lst):
    # Caso base: si la lista está vacía, retornamos 0.
    if len(lst) == 0:
        return 0
    # Caso recursivo: sumamos el primer elemento de la lista con la suma del resto de la lista.
    else:
        return lst[0] + sumaRecursiva(lst[1:])
    
# Ejemplo de uso

lista = [1, 2, 3, 4, 5]

print(f"La suma de los números en la lista es: {sumaRecursiva(lista)}")