"""
1. Pide un número al usuario. 
2. Si es positivo, imprime: "El número es positivo". 
3. Si es negativo, imprime: "El número es negativo". 
4. Si es cero, imprime: "El número es cero".

___________________________________________________

¿Qué ocurre si el usuario ingresa un texto? 
- Muestra un mensaje de error y vuelve a pedir el número.
¿Cómo adaptarías el código para números decimales?
- Cambiando el tipo de dato de int a float.
"""

# Ingreso de datos y asignación de variables

numero = int(input("Introduce un número: "))

"""# Ejecución de la estructura condicional
if not(numero.isdigit()):
    print("No has introducido un número.")
    numero = input("Introduce un número: ")
    if not(numero.isdigit()):
        print("No has introducido un número.")
        exit()

# Convertir el número a entero
numero = int(numero)"""

if numero == 0:
    print("El número es cero.")
elif numero > 0:
    print("El número es positivo.")
else:
    print("El número es negativo.")