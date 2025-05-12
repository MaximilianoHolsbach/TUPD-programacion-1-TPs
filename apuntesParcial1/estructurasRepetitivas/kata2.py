"""
• ¿Qué ocurre si el primer número ingresado es mayor que 100?
- El programa se ejecutara una vez y se detendra
• ¿Cómo evitarías errores si el usuario ingresa texto? 
- validar el tipo de dato ingresado con isdigit()
"""
# Definición de constantes
CORTE = 100

# Definición de variables
suma = 0

# Introducción de datos y asignación de variables

while suma <= 100:
    # Introducción de datos y asignación de variables   
    numero = int(input("Ingrese un número: "))
    suma += numero

print(f"El resultado de la suma es: {suma}")

