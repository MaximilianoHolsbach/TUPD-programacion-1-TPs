"""
Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función.
"""
# Definicion de la funcion

def leerEnteroValido(mensaje, min = float('-inf'), max = float('inf')):
    num = int(input(f'{mensaje}'))
    while num < min or num > max:
        num = int(input(f'Error, {mensaje}'))
    return num

def celciusAFahrenheit(celsius):
    """
    Función que convierte grados Celsius a Fahrenheit.
    :param celsius: Grados Celsius a convertir.
    :return: Grados Fahrenheit.
    """
    return (celsius * 9/5) + 32

# Programa principal

gradosCelsius = leerEnteroValido('Ingrese la temperatura en grados Celsius: ')

print(f'{gradosCelsius} grados Celsius son {celciusAFahrenheit(gradosCelsius)} grados Fahrenheit')