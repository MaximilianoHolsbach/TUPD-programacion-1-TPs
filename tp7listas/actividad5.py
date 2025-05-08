"""
Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
"""
# El codigo en cuestion elimina el mayor valor de una lista de numeros y lo imprime.
numeros = [8,15,3,22,7] # Si el valor maximo esta repetido, solo se elimina una vez, el primer valor que se encuentra en la lista.
numeros.remove(max(numeros)) # Solo se elimina el maximo valor, y no puedes convirtirlo a un string
print(numeros)

print("Fin de la actividad 5")