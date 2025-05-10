"""
LINEA |	a	 | b	| c
7	  | null | null	| null
9	  | 5	 | null	| null
8	  | 5	 |  3	| null
10	  | 5	 |  3	| 8
11	  | 2	 |  3	| 8

¿Por qué el cambio en a no afecta al valor de c?
El cambio en a no afecta al valor de c, porque c se calcula antes del cambio de a.
¿Qué pasa si se imprime a y b al final?
El valor de a será 2 y el valor de b será 3, ya que b no se ha modificado en el código.
"""

# Definicion de variables

a= 5
b = 3
c = a + 3
a = 2
print(c)

