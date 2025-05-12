"""
• ¿Cómo adaptarías el código para que el usuario elija la tabla? 
- Usando la función input() para que el usuario ingrese el número de la tabla
• ¿Qué estructura usarías para almacenar los resultados?
- Usando un ciclo for para iterar desde 1 hasta 10 y multiplicar el número ingresado por cada uno de esos valores
"""
# Ingreso de datos y asignación de variables
tabla = int(input("Ingrese un número para la tabla de multiplicar: "))

# Inicio del ciclo
for i in range(1, 11):
    print(f"{tabla} x {i} = {tabla * i}")

print("__"*20)
print("Fin del programa")
