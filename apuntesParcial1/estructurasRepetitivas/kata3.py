"""
• ¿Cómo harías que la comparación sea case-insensitive (ej: "Apple" también se cuente)? 
- Convertiria la palabra a minuscula antes de compararla
• ¿Qué método de strings es útil para esto?
- El método lower() convierte la cadena a minusculas y para comparar el caracter inicial utilizamos el metodo slicing
"""

# Definición de listas

palabras = ["apple", "banana", "Avocado", "kiwi", "mango", "pear", "peach", "plum", "grape", "orange"]

for i in range(len(palabras)):
    palabras[i] = palabras[i].lower()
    if palabras[i][0] == "a":
        print(palabras[i])

print("__"*20)
print("Fin del programa")