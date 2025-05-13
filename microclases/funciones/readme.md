*MODULARIDAD*
    Divide los problemas grandes, en pequeñas partes
*REUTILIZACION*
    Llama a la misma función varias vesces
*ABSTRACCION*
    Ocultamos cuestiones internas de resolución del problema
*MANTENIMIENTO*
    Sin tocar el resto del codigo solo mantenemos el codigo de la función

*TIPOS DE PARAMETROS DE FUNCION*
- Parametros por valor: recibe una copua del valor original, no afecta a la variable externa
```python
def incrementar(x):
```

- Parametros por referencia: referencia al objeto original. los cambios si afectan a la variable externam apunta al mismo espacion de memoria
```python
def agregarElemento(lista, elemento):
    lista.append(elemento)

miLista = [1,2,3]
agregarElemento(miLista, 4)
print(miLista)

```

*FUNCIONES INTEGRADAS EN EL LENGUAGE*

- print()
- input()
- len()

*FUNCIONES DEFINIDAS POR EL USUARIO*

```python
def obtenerResto(a,b):
    """
    Función que devuelve el resto de la división entera entre a y b.
    """
    return a % b
print(obtenerResto(10,3)) # 1
```

*COMPOSICION DE FUNCIONES*

Tomar el resultado de una función y colocarlo como argumento de otra.

```python
def siguiente(a):
    """
    Función que devuelve el siguiente número entero a.
    """
    return a + 1

def doble(a):
    """
    Función que devuelve el doble de a.
    """
    return a * 2

print(doble(siguiente(10))) # 24
```

*BUENAS PRACTICAS*

- *NOMBRES DESCRIPTIVOS*
- *UNA RESPONSABILIDAD*
- *DOCSTRINGS CLAROS*
- *EVITAR CODIGO DUPLICADO*
- *PROBAR CON CASOS LIMITE*

*AMBITOS*

- LOCAL: solo existe dentro de la funcion

- GLOBAL: se puede modificar desde cualquier punto del script

```python
a = 10
def cambiar():
    global a
    a = 20
cambiar()
print(a) # 20
```

*CLOSURES*
- Es una funcion definida dentro de otra que recuerda el entorno en el que fue creada
```python
def crearMultiplicador(n):
    def multiplicar(x)
        return x * n
    return multiplicar

doble = crearMultiplicador(2)
triple = crearMultiplicador(3)
print(doble(5)) # 20
print(triple(5)) # 30
```
Dicto prof sbruselario@frro.utn.edu.ar