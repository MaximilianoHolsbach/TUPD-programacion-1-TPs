"""
1. Pide un año al usuario. 
2. Si es divisible por 4 pero no por 100, o divisible por 400, imprime: "Se 
ingresó un año bisiesto". 
3. En otro caso, imprime: "Se ingresó un año no bisiesto". 

______________________________________________

• ¿Por qué el año 1900 no es bisiesto? 
- Porque aunque es divisible por 4, también es divisible por 100 y no es divisible por 400, lo que lo excluye de ser un año bisiesto.

¿Cómo validarías que el año sea positivo?
- Se podría agregar una validación para asegurarse de que el año ingresado sea un número entero positivo, utilizando un bucle que solicite al usuario que ingrese un año hasta que se cumpla esta condición.
"""

# Ingreso de datos y asignación de variables

anio = int(input("Introduce el año: "))

# Ejecución de la estructura condicional

if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
    print(f"El año {anio} es bisiesto.")
else:
    print(f"El año {anio} no es bisiesto.")