"""
Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
"""
# Definición de la función

def leerEnteroValido(mensaje, min = float('-inf'), max = float('inf')):
    num = input(f'{mensaje}')
    while not num.isdigit() or len(num) == 0:
        num = input(f'Error, {mensaje}')
    num = int(num) # Convertimos a entero el número
    # Validamos que el número esté dentro del rango permitido
    while num < min or num > max:
        num = int(input(f'Error, {mensaje}'))
    return num

def segundosAhoras(segundos):
    """
    Función que convierte segundos a horas, minutos y segundos.
    :param segundos: Segundos a convertir.
    :return: Tupla con horas, minutos y segundos.
    """
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos = (segundos % 3600) % 60
    return horas, minutos, segundos

# Programa principal

segundos = leerEnteroValido('Ingrese la cantidad de segundos: ', 0)

print(f'La candidad de horas equivalente es: {segundosAhoras(segundos)[0]}')

