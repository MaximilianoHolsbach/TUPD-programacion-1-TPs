"""
6) Dado un string con paréntesis "()", "{}", "[]", verifica si están correctamente
balanceados usando una pila.
Ejemplo: 
balanceado("({[]})") True
balanceado("({]}") False

"""

def balanceado(cadena):
    """
    Verifica si los paréntesis en la cadena están balanceados.
    
    Argumentos:
        cadena (str): La cadena a verificar.
    
    Returns:
        bool: True si los paréntesis están balanceados, False en caso contrario.
    """
    pila = []
    pares = {')': '(', '}': '{', ']': '['}
    
    for caracter in cadena:
        if caracter in pares.values():
            pila.append(caracter)
        elif caracter in pares.keys():
            if not pila or pares[caracter] != pila.pop():
                return False
    return len(pila) == 0

balanceado1 = balanceado("({[})")
print(f"Cadena balanceada: {balanceado1}")
balanceado2 = balanceado("({[]})")
print(f"Cadena balanceada: {balanceado2}")