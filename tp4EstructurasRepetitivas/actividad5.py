"""Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número."""
from random import randint

print("Bienvenido al juego de adivinar el número")
print("He pensado un número entre 1 y 9, ¿puedes adivinarlo?")
corte = True 
numero_secreto = randint(0, 9)
intentos = 0

while corte:
    numeroUsuario = int(input("Introduce un número entre 1 y 9: "))
    intentos += 1
    if intentos > 5:
        print(f'Has agotado tus intentos. El número era {numero_secreto}.')
    corte = input("¿Quieres seguir jugando? (s/n): ").lower() == 's'

print(f'¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.')

print("Gracias por jugar.")