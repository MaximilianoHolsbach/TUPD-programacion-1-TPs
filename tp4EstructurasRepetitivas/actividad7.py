"""Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario."""
numeroUsuario = int(input("Ingrese un número entero positivo: "))
suma = 0

if numeroUsuario <= 0:
    print("El número ingresado no es positivo, o es cero")
else:
    for i in range(numeroUsuario + 1):
        suma += i
    print(f"La suma de los números enteros desde 0 hasta {numeroUsuario} es: {suma}")