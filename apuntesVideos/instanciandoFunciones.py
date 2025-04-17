import funcionesVarias # Importamos el módulo funcionesVarias

# Ingresamos dos números enteros por teclado
numero1 = int(input("Introduce un número: "))
numero2 = int(input("Introduce otro número: ")) 

# Invocamos las funciones del módulo funcionesVarias
resto = funcionesVarias.obtenerResto(numero1, numero2)
print(f"El resto de {numero1} entre {numero2} es: {resto}")

if funcionesVarias.esMultipo(numero1, numero2):
    print(f"{numero1} es múltiplo de {numero2}")
else:
    print(f"{numero1} no es múltiplo de {numero2}")

