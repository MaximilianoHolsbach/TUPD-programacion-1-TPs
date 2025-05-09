"""
Las listas son secuencias mutables ya que permiten modificar los valores de sus elementos, eliminar o añadir elementos.
En ellas se pueden almacenar tantos elementos como se desee, incluso pueden existir listas vacías (sin elementos). Para definirlas se utilizan corchetes y se separan los elementos mediante comas :
"""
nombreLista = [9.1,8.5,7.3]
print(f"nombreLista = {nombreLista}") # [9.1, 8.5, 7.3]
print(f"tipo de dato = {type(nombreLista)}") # <class 'list'>

# No es necesario que una lista contenga el mismo tipo de datos. Por ejemplo, podemos tener la siguiente lista:

nombreLista = [9.1,8.5,7.3,"Hola",True]
print(f"nombreLista = {nombreLista}") # [9.1, 8.5, 7.3]
print(f"tipo de dato = {type(nombreLista)}") # <class 'list'>

print("**********************")
print("* Métodos con listas *")
print("**********************")


# Se puede crear una lista de números automáticamente utilizando range(inicio, fin).

print("Creando una lista de números automáticamente utilizando range(inicio, fin)")

listasRange = list(range(1,10)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"listasRange = {listasRange}") # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Por default toma intervalos de 1 en 1. Para modificar esto basta con agregar un argumento a range(inicio, fin, intervalo).

print("Creando una lista de números automáticamente utilizando range(inicio, fin, intervalo)")
listasRange = list(range(1,10,2)) # [1, 3, 5, 7, 9]

# split: Permite crear una lista a partir de un string, utilizando un caracter específico como separador. Por defecto, utiliza los espacios para separar el string en distintos elementos de la lista.
print("Creando una lista a partir de un string utilizando split()")
nombreLista = "Hola soy un string"
nombreLista = nombreLista.split() # ['Hola', 'soy', 'un', 'string']
print(f"nombreLista = {nombreLista}") # ['Hola', 'soy', 'un', 'string']

# Slicing: Es posible acceder a los distintos elementos de una lista utilizando el índice del mismo, de manera análoga a como se realiza con los strings nombre_lista[índice_elemento].

print("Accediendo a los distintos elementos de una lista utilizando el índice del mismo")
nombreLista = [9.1,8.5,7.3,"Hola",True]
print(f"nombreLista[0] = {nombreLista[0]}") # 9.1
print(f"nombreLista[1] = {nombreLista[1]}") # 8.5
print(f"tipoNombreLista[2] = {type(nombreLista[2])}") # <class 'float'>
print(f"RangoNombreLista[0:3] = {nombreLista[0:3]}") # [9.1, 8.5, 7.3]

"""
Añadir elementos
Se usa la sentencia nombreLista.append(elementoAAñadir).
Notar que no es necesario sobreescribir la variable, las sentencia append() modifica la lista sin necesidad de sobreescribirla.
"""
print("Añadiendo elementos a la lista utilizando append()")
nombreLista = [9.1,8.5,7.3,"Hola",True]
print(f"nombreLista = {nombreLista}") # [9.1, 8.5, 7.3, 'Hola', True]
nombreLista.append("Nuevo elemento")
print(f"nombreLista = {nombreLista}") # [9.1, 8.5, 7.3, 'Hola', True, 'Nuevo elemento']

"""
Eliminar elementos
Se usa la sentencia nombreLista.remove(elementoAEliminar).
"""
print("Eliminando elementos de la lista utilizando remove()")
nombreLista = [9.1,8.5,7.3,"Hola",True]
print(f"nombreLista = {nombreLista}") # [9.1, 8.5, 7.3, 'Hola', True]
nombreLista.remove(8.5)
print(f"nombreLista = {nombreLista}") # [9.1, 7.3, 'Hola', True]

"""
Actualizar elementos
Para esto se hace uso del slicing. Esta operación diferencia una lista de un string, ya que no puede ser efectuada en el segundo tipo de dato. <Por ejemplo, si queremos actualizar el tercer elemento:
"""
print("Actualizando elementos de la lista utilizando slicing")
nombreLista = [9.1,8.5,7.3,"Hola",True]
print(f"nombreLista = {nombreLista}") # [9.1, 8.5, 7.3, 'Hola', True]
nombreLista[2] = 10.5
print(f"nombreLista = {nombreLista}") # [9.1, 8.5, 10.5, 'Hola', True]

"""
Concatenación
Se pueden concatenar dos listas usando el operador de la suma (+).
"""
print("Concatenando listas utilizando el operador de la suma (+)")
nombreLista1 = [9.1,8.5,7.3,"Hola",True]
nombreLista2 = [1,2,3,4,5]
print(f"nombreLista1 = {nombreLista1}") # [9.1, 8.5, 7.3, 'Hola', True]
print(f"nombreLista2 = {nombreLista2}") # [1, 2, 3, 4, 5]
nombreLista3 = nombreLista1 + nombreLista2
print(f"nombreLista3 = {nombreLista3}") # [9.1, 8.5, 7.3, 'Hola', True, 1, 2, 3, 4, 5]

"""
Comprobar si un valor existe dentro de la lista
Se usa el término in.
"""
print("Comprobando si un valor existe dentro de la lista utilizando in")
nombreLista = [9.1,8.5,7.3,"Hola",True]
print(f"nombreLista = {nombreLista}") # [9.1, 8.5, 7.3, 'Hola', True]
print(f"8.5 in nombreLista = {8.5 in nombreLista}") # True

"""
LISTAS ANIDADAS
Pueden haber listas adentro de otras listas, por ejemplo:
"""
print("Creando listas anidadas")
nombreLista = [9.1,8.5,7.3,"Hola",True,[1,2,3,4,5]]
print(f"nombreLista = {nombreLista}") # [9.1, 8.5, 7.3, 'Hola', True, [1, 2, 3, 4, 5]]
print(f"nombreLista[5] = {nombreLista[5]}") # [1, 2, 3, 4, 5]
print(f"nombreLista[5][0] = {nombreLista[5][0]}") # 1

"""
Recorriendo los elementos de una lista con el bucle for
"""
print("Recorriendo los elementos de una lista con el bucle for")
nombreLista = [9.1,8.5,7.3,"Hola",True]
print(f"nombreLista = {nombreLista}") # [9.1, 8.5, 7.3, 'Hola', True]
for i in nombreLista:
    print(f"i = {i}") # 9.1, 8.5, 7.3, Hola, True
print("Fin del recorrido")

rango = list(range(0,10,2))

print(f"rango = {rango}") # [0, 2, 4, 6, 8]

nuevaLista = "uno-dos-tres".split("-")
print(f"nuevaLista = {nuevaLista}") # ['uno', 'dos', 'tres']

nums = [10,20,30,40,50]
print(f"nums = {nums[1:4]}") # [20, 30, 40]

caracteres = ["p","q","r","s"]
print(f"caracteres = {caracteres[0:2]}") # ['p', 'q']

listaCuestionario = [1,2,3,4,5,6,7,8,9,10]

a = [9.1, 8.5] 
b = ['UTN', True]
nueva=a + b
print(f"nueva = {nueva}") # [9.1, 8.5, 'UTN', True]

