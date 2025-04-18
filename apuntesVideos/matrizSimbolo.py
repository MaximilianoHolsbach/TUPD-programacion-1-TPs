import funcionesVarias

# Programa principal

columnas = funcionesVarias.leerEnteroValido('Ingrese la cantidad de columnas de la matriz: ', 1, 10)
filas = funcionesVarias.leerEnteroValido('Ingrese la cantidad de filas de la matriz: ', 1, 10)
simbolo = input('Ingrese el símbolo a utilizar: ')

funcionesVarias.imprimirMatrizSimbolos(columnas, filas, simbolo)
