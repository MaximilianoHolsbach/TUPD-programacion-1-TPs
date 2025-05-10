"""
1. Solicitar al usuario su peso en kg y su altura en metros.
2. Calcular el IMC con la fórmula: IMC = peso / (altura ** 2).
3. Mostrar el resultado con un mensaje como: "Tu IMC es: 22.5".

• ¿Qué rango se considera saludable para el IMC?
- Un IMC entre 18.5 y 24.9 se considera saludable.
• ¿Cómo podrías dar una recomendación según el resultado?
- Podria utilizar un operador condicional para determinar si el IMC está dentro del rango saludable y dar una recomendación.
"""

# Definicion de variables

nombre = input("Ingrese su nombre: ")

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
# Definicion de operaciones
imc = peso / (altura ** 2) 
# Definicion de salida
print(f"Hola {nombre}, tu IMC es: {imc:.2f}")
if 18.5 <= imc <= 24.9:
    print("Tu IMC está dentro del rango saludable.")
else:
    print("Tu IMC no está dentro del rango saludable.")