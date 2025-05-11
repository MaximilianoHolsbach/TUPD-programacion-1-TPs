"""
1. Solicita dos números al usuario. 
2. Si el primero es mayor, imprime: "El primer número ingresado es mayor". 
3. Si el primero es menor, imprime: "El primer número ingresado es menor". 
4. Si son iguales, imprime: "Los números ingresados son iguales".

___________________________________________________________________________

• ¿Cómo modificarías el programa para comparar más de dos números? 
- Se podría usar una lista y un bucle para comparar todos los números.
• ¿Qué pasa si se ingresan valores no numéricos?
- El programa lanzará un error de tipo (TypeError) al intentar convertir un texto a un número.
"""

# Ingreso de datos y asignación de variables

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

# Ejecución de la estructura condicional

if numero1 == numero2:
    print("Los números son iguales.")
elif numero1 > numero2:
    print("El primer número es mayor que el segundo.")
else:
    print("El segundo número es mayor que el primero.")

