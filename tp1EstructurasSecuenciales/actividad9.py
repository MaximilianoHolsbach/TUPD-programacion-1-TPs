"""
9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
F = C * 9/5 + 32
"""
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = celsius * 9/5 + 32
print(f"La temperatura en grados Fahrenheit es: {fahrenheit}")