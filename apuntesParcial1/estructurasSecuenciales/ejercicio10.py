"""
• ¿Qué ocurre si el descuento es mayor a 100%?
- En este script el precio final es cero. En casos podria se negativo.
• ¿Cómo podrías mostrar el monto ahorrado?
- Podria calcular el monto ahorrado restando el precio final al precio original y mostrarlo como un mensaje adicional.
"""

# Definicion de variables

precio = float(input("Ingrese el precio del producto: "))
descuento = (int(input("Ingrese el porcentaje de descuento: ")))/100
precioFinal = precio - (precio * descuento)
# Definicion de salida
print(f"El precio final del producto es: {precioFinal:.2f}")
print(f"El monto ahorrado es: {precio - precioFinal:.2f}")