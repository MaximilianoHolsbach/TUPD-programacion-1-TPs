"""
Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.
"""
# Definicion de funciones

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

def informacion_personal():
    """
    Esta función solicita al usuario su nombre, edad y ciudad de residencia,
    e imprime un mensaje con esa información.
    """
    nombre = validarCadena("Ingrese su nombre: ", 1)
    edad = leerEnteroValido("Ingrese su edad: ",1)
    ciudad = validarCadena("Ingrese su ciudad de residencia: ", 1)

    print(f"Hola, {nombre}. Tienes {edad} años y vives en {ciudad}.")

# Programa principal

datosPersonales =  informacion_personal()