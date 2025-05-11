"""
• ¿Cómo adaptarías el programa para usar °F? 
- Se podría agregar una opción para que el usuario elija la unidad de temperatura (Celsius o Fahrenheit) y luego convertir la temperatura ingresada a Celsius para realizar la comparación.

• ¿Qué considerarías para añadir más rangos (ej: "Hace mucho frío")?
- Se podrían definir más rangos de temperatura y sus respectivas descripciones, como "Hace mucho frío" para temperaturas por debajo de 0°C o "Hace calor extremo" para temperaturas superiores a 35°C.
"""

# Ingreso de datos y asignación de variables

temperatura = float(input("Introduce la temperatura en grados Celsius: "))

# Ejecución de la estructura condicional

if temperatura <= 10:
    print(f"La temperatura es {temperatura}°C, hace frío.")
elif 10 < temperatura <= 25:
    print(f"La temperatura es {temperatura}°C, esta templado.")
elif temperatura < 25:
    print(f"La temperatura es {temperatura}°C, hace calor.")
else:
    print("La temperatura es incorrecta.")