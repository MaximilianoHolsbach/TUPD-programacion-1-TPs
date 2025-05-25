"""
Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.
Restricciones:
No se puede convertir el número a string.
Usá operaciones matemáticas (%, //) y recursión.
"""


def sumaDigitos(numero):
    if numero == 0 :
        return 0
    else:
        digito = numero % 10
        return digito + sumaDigitos(numero // 10)
    
# Ejemplo de uso

numero = 12345

resultado = sumaDigitos(numero)

print(f"La suma de los dígitos de {numero} es: {resultado}")
