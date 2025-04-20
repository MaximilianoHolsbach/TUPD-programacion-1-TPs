"""
5) Crear una clase llamada Circulo que contenga el atributo radio y los métodos calcular_area y
calcular_perimetro. Dichos métodos deben calcular el parámetro correspondiente.
Ayuda: el módulo math puede ser de utilidad para usar la constante 𝜋.
"""

import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return round(math.pi * self.radio ** 2,2)

    def perimetro(self):
        return round(2 * math.pi * self.radio,2)
    
circulo1 = Circulo(5)
print(f"Área del círculo: {circulo1.area()}")
print(f"Perímetro del círculo: {circulo1.perimetro()}")

