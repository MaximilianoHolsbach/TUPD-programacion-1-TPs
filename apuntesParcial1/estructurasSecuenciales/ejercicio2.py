"""
Realizar la conversión de temperatura de Celsius a Fahrenheit. 
1. Solicitar al usuario una temperatura en grados Celsius. 
2. Convertirla a Fahrenheit con la fórmula: F = (C * 9/5) + 32. 
3. Mostrar el resultado en pantalla. 
Preguntas de reflexión:
¿Qué resultado se obtiene al ingresar 0°C? 
La temperatura en Fahrenheit es: 32.0
¿Cómo se adaptaría este ejercicio para convertir a Kelvin? 
Hay que sumar 273.15 a la temperatura en celsius ingresada por el usuario.
"""

# Ingreso de datos

grados = float(input("Ingrese la temperatura en grados Celsius: "))

# Calculo de la temperatura en Fahrenheit

farenheit = (grados * 9/5) + 32

print(f"La temperatura en Fahrenheit es: {farenheit}")

# Calculo de la temperatura en Kelvin

kelvin = grados + 273.15

print(f"La temperatura en Kelvin es: {kelvin}")

