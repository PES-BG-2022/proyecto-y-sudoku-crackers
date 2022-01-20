import numpy as np

def parsemap(filename: str):
    with open(filename) as f:
        input = f.readlines()
    sudoku = []
    for s in input: 
        row = []
        for c in s: 
            if c != "\n": row.append(int(c))
        sudoku.append(row)
    return np.array(sudoku)

#posibilidades
def posibilidad (fila, columna, numero, sudoku):
     #Chequeando si el numero aparece en la fila
    for i in range (0,9):
        if sudoku[fila][i] == numero:
            return False

    #chequeando si el numero aparece en la columna
    for i in range (0,9):
        if sudoku[i][columna] == numero:
            return False

    #chequear si esta en el cuadro de 3x3
    x = (fila // 3) * 3
    y = (columna // 3) * 3

    #haciendo la verificacion
    for i in range (0,3):
        for j in range(0,3):
            #x y y, es la posicion inicial (sumando i chequea los otros 2):
            if sudoku[x+i][y+j] == numero:
                return False
    return True

# solucion
def sol(sudoku):
    #verificar que no tenga valor la casilla, si no tiene valor es 0
    m=sudoku.shape[0]
    n=sudoku.shape[1]


    for x in range(m):
        for y in range(n):
            if sudoku[x][y] == 0:
                #prueba valores de 1-9, usando la funcion posibilidad, lo llena y si hay un punto que no puede avanzar mas
                #usa la recursividad para regresar y probar otros valores, hasta encontrar la solucion
                for valor in range (1,10):
                    if posibilidad(x, y, valor, sudoku):
                        sudoku[x][y] = valor
                        sol(sudoku)
                        sudoku[x][y] = 0
                return
    print(sudoku)
    return

def resolver(filename):
    sudoku = parsemap(filename)
    solucion = sol(sudoku)

    return solucion


#aqui debe añadirse como recibe el sudoku el programa

if __name__ == "__main__": 
    resolver("sudoku.txt")


#sol(a)