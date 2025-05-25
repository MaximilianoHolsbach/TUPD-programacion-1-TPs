"""

"""

def contarDigito(numero, digito):
    if numero == 0:
        return 0
    else:
        if numero % 10 == digito:
            return 1 + contarDigito(numero // 10, digito)
        else:
            return contarDigito(numero // 10, digito)
        
# Ejemplo de uso

numero = int(input("Introduce un número entero: "))
digito = int(input("Ingresa el digito y descubre cuantas veces aparece en el numero ingresado: "))

print(f"El digito {digito} aparece {contarDigito(numero, digito)} veces en el numero {numero}.")
