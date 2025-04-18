"""
Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

"""
# Definición de la función

def leerEnteroValido(mensaje, min = float('-inf'), max = float('inf')):
    num = int(input(f'{mensaje}'))
    while num < min or num > max:
        num = int(input(f'Error, {mensaje}'))
    return num

def operacionesBasicas(num1, num2):
    """
    Función que realiza las operaciones básicas (suma, resta, multiplicación y división) entre dos números.
    :param num1: Primer número.
    :param num2: Segundo número.
    :return: Tupla con los resultados de las operaciones.
    """
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2 if num2 != 0 else 'Error: División por cero'
    return suma, resta, multiplicacion, division

# Programa principal

numero1 = leerEnteroValido('Ingrese el primer número: ')
numero2 = leerEnteroValido('Ingrese el segundo número: ')

resultado = operacionesBasicas(numero1, numero2)

print(f'Suma: {resultado[0]} \nResta: {resultado[1]} \nMultiplicación: {resultado[2]} \nDivisión: {resultado[3]}')


