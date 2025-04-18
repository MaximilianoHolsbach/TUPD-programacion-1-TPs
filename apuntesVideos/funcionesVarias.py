#Definición de funciones del video https://www.youtube.com/watch?v=coeuXXCoVl4&t=614s perteneciente a la ACTIVIDAD II

def obtenerResto(dividendo, divisor):
    """
    Función que obtiene el resto de una división entera.
    :param dividendo: Número entero que se va a dividir.
    :param divisor: Número entero por el cual se va a dividir.
    :return: Resto de la división entera.
    """
    return dividendo % divisor


def suma(num1, num2):
    """
    Función que suma dos números.
    :param num1: Primer número a sumar.
    :param num2: Segundo número a sumar.
    :return: Suma de los dos números.
    """
    return num1 + num2

def esMultipo(num1, num2): # En este caso utilizamos el uso de composición de funciones
   """
    Función que determina si un número es múltiplo de otro.
    param num1: Número que se va a comprobar si es múltiplo.
    param num2: Número por el cual se va a comprobar si es múltiplo.
    return: True si num1 es múltiplo de num2, False en caso contrario.
    """
   return obtenerResto(num1, num2) == 0

def leerEnteroValido(mensaje, min = float('-inf'), max = float('inf')):
    num = input(f'{mensaje}')
    while not num.isdigit() or len(num) == 0:
        num = input(f'Error, {mensaje}')
    num = int(num) # Convertimos a entero el número
    # Validamos que el número esté dentro del rango permitido
    while num < min or num > max:
        num = int(input(f'Error, {mensaje}'))
    return num

def validarCadena(mensaje, min = float('-inf'), max = float('inf')):
    """
    Funcion que valida una cadena de texto.
    :param mensaje: Mensaje a mostrar al usuario.
    :param min: Longitud mínima de la cadena.
    :param max: Longitud máxima de la cadena.
    :return: Cadena de texto validada.
    """
    cadena = input(mensaje)
    while len(cadena) < min or len(cadena) > max:
        cadena = input(f'Error. {mensaje}')
    return cadena

def esPrimo(numero1):
    cont = 2
    numero1 = numero1 // 2 # Dividimos entre 2 el número para optimizar el proceso
    while cont <= numero1 and not(esMultipo(numero1, cont)):
        cont += 1
    return cont > numero1 # Si el contador es igual al número, es primo

def informarSiEsPrimo(num1):
    if esPrimo(num1):
        print(f'El número {num1} es primo')
    else:
        print(f'El número {num1} no es primo')

def sumaDivisoresPropios(num1):
    suma = 0
    for i in range(1, (num1 // 2) + 1):
        if esMultipo(num1, i):
            suma = suma + i
    return suma

def esPerfecto(num1):
    return sumaDivisoresPropios(num1) == num1

def informarSiEsPerfecto(num1):
    if esPerfecto(num1):
        print(f'El número {num1} es perfecto')
    else:
        print(f'El número {num1} no es perfecto')

def sucesionSimbolos(simbolo, cantidad):
    sucecion = ''
    for i in range(cantidad):
        sucecion += simbolo
    return sucecion

def imprimirSimbolo(simbolo, cantidad):
    print(sucesionSimbolos(simbolo, cantidad))

def imprimirMatrizSimbolos(columnas, filas, simbolo = 'X'):
    for i in range(filas):
        imprimirSimbolo(simbolo, columnas)

def calcularAreaCirculo(radio):
    """
    Función que calcula el área de un círculo dado su radio.
    :param radio: Radio del círculo.
    :return: Área del círculo.
    """
    return 3.14 * (radio ** 2) # Usamos 3.14 como aproximación de pi

def calcularPerimetroCirculo(radio):
    """
    Función que calcula el perímetro de un círculo dado su radio.
    :param radio: Radio del círculo.
    :return: Perímetro del círculo.
    """
    return 2 * 3.14 * radio # Usamos 3.14 como aproximación de pi