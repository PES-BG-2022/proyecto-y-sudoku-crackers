import numpy as np
def parsemap(filename: str):
    """Obtiene un np.ndarray para representar el mapa de energías desde el
    archivo filename"""
    with open(filename) as f:
        input = f.readlines()
    energymap = []
    for s in input: 
        row = []
        for c in s: 
            if c != "\n": row.append(int(c))
        energymap.append(row)
    return np.array(energymap)
    

#imprimir sudoku
def imprimir(a):
    for l in a:
        print(l)


#posibilidades
def posibilidad (fila, columna, numero, a):
     #Chequeando si el numero aparece en la fila
    for i in range (0,9):
        if a[fila][i] == numero:
            return False
    #chequeando si el numero aparece en la columna
    for i in range (0,9):
        if a[i][columna] == numero:
            return False
    #chequear si esta en el cuadro de 3x3
    x = (fila // 3) * 3
    y = (columna // 3) * 3
    #haciendo la verificacion
    for i in range (0,3):
        for j in range(0,3):
            #x y y, es la posicion inicial (sumando i chequea los otros 2):
            if a[x+i][y+j] == numero:
                return False
    return True
# solucion
def sol(sudoku):
    m = sudoku.shape[0]
    n = sudoku.shape[1]
    #verificar que no tenga valor la casilla, si no tiene valor es 0
    for x in range(m):
        for y in range(n):
            if sudoku[x][y] == 0:
                #prueba valores de 1-9, usando la funcion posibilidad, lo llena y si hay un punto que no puede avanzar mas
                #usa la recursividad para regresar y probar otros valores, hasta encontrar la solucion
                for valor in range (1,10):

                    if posibilidad(x, y, valor, sudoku):
                        sudoku[x][y] = valor
                        solucionador = sol(sudoku)[0]
                        if solucionador:
                            return (True,sudoku)
                        sudoku[x][y] = 0
                return (False,sudoku)
    #print(sudoku)
    return (True,sudoku)


if __name__ == "__main__": 
    sudoku = parsemap("sodokudificil1.txt")
    print(sudoku)
    solucion =  sol(sudoku)[1]
    print(solucion)
