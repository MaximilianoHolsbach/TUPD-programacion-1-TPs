"""
Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
"""
# Definición de la función

def leerDecimalValido(mensaje, min = float('-inf'), max = float('inf')):
    num = float(input(f'{mensaje}'))
    while num < min or num > max:
        num = float(input(f'Error, {mensaje}'))
    return num

def calcularImc(peso, altura):
    """
    Función que calcula el índice de masa corporal (IMC) dado el peso y la altura.
    :param peso: Peso en kilogramos.
    :param altura: Altura en metros.
    :return: IMC.
    """
    return peso / (altura ** 2)

# Programa principal

peso = leerDecimalValido('Ingrese su peso: ', 1, 500)
altura = leerDecimalValido('Ingrese su altura: ', 1, 3)

print(f'El IMC es: {calcularImc(peso, altura)}') 