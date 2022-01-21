from operator import mod
import numpy as np
import os

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

class casilla:
    def __init__(self,sudoku,x,y): #debe ingresarse solamente el sudoku sin resolver
        self.sudoku = sudoku
        self.x = x
        self.y = y
        self.posibilidades = []
        valor = self.sudoku[self.x][self.y]
    def get_Posibilidades(self):
        for i in range(1,10):        
            if posibilidad(self.x,self.y,i,self.sudoku):
                self.posibilidades.append(i)
        return self.posibilidades


def matriz_posibilidad(sudoku):
    solucion = sudoku.copy()
    casillas = []
    for x in range(0,solucion.shape[0]):
        row = []
        for y in range(0,solucion.shape[1]):
            #print(f"la casilla {x},{y} tiene un {solucion[x][y]}")
            posibilidades = []
            if solucion[x][y]==0:
                #print(f"entra aqui ({x},{y}), el valor de esta casilla es {solucion[x][y]}")
                posibilidades = casilla(solucion,x,y).get_Posibilidades()
            row.append(posibilidades)
        casillas.append(row)
    matriz = np.array(casillas,dtype=object)
    return matriz

def escoger_posiblidad2(sudoku):
    print("empieza escoger posibilidades UNICAS")
    matriz = matriz_posibilidad(sudoku)
    temp_solucion = sudoku.copy()
    temp_matriz = matriz.copy()
    print(temp_solucion)
    for x in range(temp_solucion.shape[0]):
        for y in range(temp_solucion.shape[1]):
            #if temp_matriz[x][y]!=[] and temp_solucion[x][y]==0:
            if temp_matriz[x][y]!=[] and temp_solucion[x][y]==0:
                
                mod_solucion = temp_solucion.copy()
                for i in temp_matriz[x][y]:
                    volver_iterar = False
                    #if volver_iterar: break
                    print(f"las posibilidades de ({x},{y}) son {temp_matriz[x][y]}")
                    print(f"probando con {i}")
                    
                    
                    #mod_matriz = temp_matriz.copy()
                    mod_solucion[x][y]=i
                    mod_matriz = matriz_posibilidad(mod_solucion)
                    print(mod_solucion)
                    print(f"las posibilidades de ({x},{y}) son {mod_matriz[x][y]}")  

                    #comprobar que existan posibilidades para los demas ceros

                    for fila in range(mod_solucion.shape[0]):
                        for columna in range(mod_solucion.shape[1]):
                            if mod_matriz[fila][columna]==[] and mod_solucion[fila][columna]==0: #si una list es vacia, retorna falso
                                print(f"las posibilidades de ({fila},{columna}) son: {mod_matriz[fila][columna]}) AAAA")
                                print("no funciono, seguir iterando")
                                volver_iterar = True
                            if volver_iterar: break
                            #else: escoger_posiblidad2(temp_solucion) #si no funciona vuelve a intentar
                        if volver_iterar: break
                    if not volver_iterar: break #esto evita que siga probando numeros de los posibles
                    else: #si se indica que vuelva a iterar
                        mod_solucion = temp_solucion.copy()
                        #temp_matriz = matriz_pre.copy()
                        pass
                        

            elif temp_matriz[x][y]==[] and temp_solucion[x][y]==0:print(f"Cero sin solucion {temp_matriz[x][y]}")
        
    
    return temp_solucion


def escoger_posibilidad_unica2(sudoku):
    
    matriz = matriz_posibilidad(sudoku)
    print("empieza escoger posibilidades")
    print(matriz)
    temp_solucion = sudoku.copy()
    temp_matriz = matriz.copy()
    print(temp_solucion)


    #primero debe guardar los valores que solamente tienen una posibilidad
    for x in range(temp_solucion.shape[0]):
        for y in range(temp_solucion.shape[1]):
            if len(temp_matriz[x][y])==0 and temp_solucion[x][y]==0:
                print(f"NO PUEDE SER ({x},{y}) son {temp_matriz[x][y]}")
                return sudoku
                #print("NO PUEDE SER")
            elif len(temp_matriz[x][y])==1 and temp_solucion[x][y]==0: 
                temp_solucion[x][y] = temp_matriz[x][y][0]
                print(f"Las posibilidades de ({x},{y})")
                print(f"son {temp_matriz[x][y][0]}")
                print(temp_solucion)
                temp_matriz = matriz_posibilidad(temp_solucion)

    #ahora debe escogerse entre las posibilidades restantes
    return temp_solucion


def escoger_posibilidad_unica(sudoku):
    
    matriz = matriz_posibilidad(sudoku)
    print("empieza escoger posibilidades")
    print(matriz)
    temp_solucion = sudoku.copy()
    temp_matriz = matriz.copy()
    print(temp_solucion)


    #primero debe guardar los valores que solamente tienen una posibilidad
    for x in range(temp_solucion.shape[0]):
        for y in range(temp_solucion.shape[1]):
            if len(temp_matriz[x][y])==0 and temp_solucion[x][y]==0:
                print(f"NO PUEDE SER ({x},{y}) son {temp_matriz[x][y]}")
                return sudoku
                #print("NO PUEDE SER")
            elif len(temp_matriz[x][y])==1 and temp_solucion[x][y]==0: 
                temp_solucion[x][y] = temp_matriz[x][y][0]
                print(f"Las posibilidades de ({x},{y})")
                print(f"son {temp_matriz[x][y][0]}")
                print(temp_solucion)
                temp_matriz = matriz_posibilidad(temp_solucion)

    for x in range(temp_solucion.shape[0]):
        for y in range(temp_solucion.shape[1]):
            if len(temp_matriz[x][y])==0 and temp_solucion[x][y]==0:
                print("Aqui se accede si se vuelven a generar posibilidades unicas")
                return escoger_posibilidad_unica(temp_solucion)

    #ahora debe escogerse entre las posibilidades restantes
    return temp_solucion


def escoger_posibilidad_mult(sudoku):
    sudoku = escoger_posibilidad_unica(sudoku)
    matriz = matriz_posibilidad(sudoku)
    print("POSIBILIDADES MULTIPLES")
    temp_solucion = sudoku.copy()
    temp_matriz = matriz.copy()

    mod_solucion = temp_solucion.copy()
    mod_matriz = temp_matriz.copy()

    for x in range(mod_solucion.shape[0]):
        for y in range(mod_solucion.shape[1]):
            if len(temp_matriz[x][y])==2 and mod_solucion[x][y]==0: 
                
                for i in temp_matriz[x][y]:
                    print(f"Las posibilidades de ({x},{y}) son {temp_matriz[x][y]}")
                    print(f"probando con {i}")
                    volver_iterar = False
                    mod_solucion[x][y]=i
                    post_solucion = escoger_posibilidad_unica(mod_solucion)

                    if (mod_solucion == post_solucion).all():
                        print("Esta no era la respuesta, se debe volver a iterar")
                        volver_iterar = True
                        continue
                    else:
                        print(f"Efectivamente era buena eleccion colocar {i} en ({x},{y}) de todos los posibles valores {temp_matriz[x][y]}")
                        
                        mod_solucion = post_solucion
                        
                        mod_matriz=matriz_posibilidad(mod_solucion)
                        print(mod_matriz)
                        temp_matriz = mod_matriz #pruebas
                        #
                        #print(mod_solucion)
                        break

    return escoger_posibilidad_unica(mod_solucion)


def matriz_posibil(sudoku):
    mas_posibilidades = False
    solucion = sudoku.copy()
    casillas = []
    for x in range(0,solucion.shape[0]):
        row = []
        for y in range(0,solucion.shape[1]):
            #print(f"la casilla {x},{y} tiene un {solucion[x][y]}")
            posibilidades = []
            if solucion[x][y]==0:
                #print(f"entra aqui ({x},{y}), el valor de esta casilla es {solucion[x][y]}")
                posibilidades = casilla(solucion,x,y).get_Posibilidades()
                
                #print(f" las posibilidades son {posibilidades}")
                
                if posibilidades:
                    #error al resolver el sudoku, no deberia llegar aqui        
                    if len(posibilidades)==1:
                        #print(f"se modificara la casilla {x},{y} de un {solucion[x][y]}")
                        #print(solucion)
                        solucion[x][y]=posibilidades[0]
                        #print(f"se modificara la casilla ({x},{y}) a un {solucion[x][y]}")
                        #print(solucion)
                        #return matriz_posibil(solucion)
                    else: 
                        mas_posibilidades = True
                else: 
                    print(f" las posibilidades son {posibilidades}")
                    print("Esto es un problema")
                    print(solucion)
                    #return matriz_posibil(escoger_posiblidad(matriz,solucion))
 

            row.append(posibilidades)
        casillas.append(row)
    matriz = np.array(casillas,dtype=object)
    #print(solucion)

    if(solucion==sudoku).all():
            print(solucion)
            print("ya no existe una sola posibilidad UNICA para continuar")
            #COMPROBAR ITEM VACIO
            if mas_posibilidades: 
                print("debe escogerse una de las posibilidades")
                return matriz_posibil(escoger_posiblidad(matriz,solucion)) # matriz_posibil()
            else:
                print("YA NO PUEDE CONTINUAR") 
                return solucion

    else:
            print("Se vuelve a realizar")
            return matriz_posibil(solucion)    
            
def escoger_posiblidad(matriz,solucion):
    print("empieza escoger posibilidades")
    temp_solucion = solucion.copy()
    temp_matriz = matriz.copy()
    for x in range(temp_matriz.shape[0]):
        for y in range(temp_matriz.shape[1]):
            if temp_matriz[x][y]!=[]:
                
                for i in temp_matriz[x][y]:
                    volver_iterar = False
                    print(f"las posibilidades de ({x},{y}) son {temp_matriz[x][y]}")
                    print(f"probando con {i}")
                    temp_solucion[x][y]=i
                    matriz_temp = matriz_posibil(temp_solucion)
                    print(temp_solucion)  
                    for fila in range(temp_solucion.shape[0]):
                        for columna in range(temp_solucion.shape[1]):
                            if not matriz_temp[fila][columna]: #si una list es vacia, retorna falso
                                print("no funciono, seguir iterando")
                                volver_iterar = True
                                break
                            if volver_iterar: break
                        if volver_iterar: break
                return temp_solucion
                    

                    

    
    pass    



#posibilidades
def posibilidad(fila, columna, numero, sudoku):
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
def sol(sudoku : np.array):
    solucion = sudoku.copy()
     
    m=solucion.shape[0]
    n=solucion.shape[1]
    
    #verificar que no tenga valor la casilla, si no tiene valor es 0
    for x in range(m):
          
        for y in range(n):
            
            if solucion[x][y] == 0:
                #prueba valores de 1-9, usando la funcion posibilidad, lo llena y si hay un punto que no puede avanzar mas
                #usa la recursividad para regresar y probar otros valores, hasta encontrar la solucion
                for valor in range (1,10):
                    print(solucion)
                    if posibilidad(x, y, valor, solucion):
                        solucion[x][y] = valor
                        sol(solucion)
                        solucion[x][y] = 0
                        
                    
                    return
             
    print(solucion)
    return 





def resolver(filename:str):
    
    sudoku = parsemap(filename)
    #print(sudoku)

    #print(f"Los posibles valores son:\n{matriz_posibilidad(sudoku)}")
    #print(f"LA SOLUCION ES:\n{escoger_posiblidad3(sudoku)}")
    
    #escoger_posibilidad_unica(sudoku)
    return escoger_posibilidad_mult(sudoku)
    #solucion = sol(sudoku)
    #return solucion


#aqui debe añadirse como recibe el sudoku el programa

if __name__ == "__main__": 
    #os.system('cls') 
    print("La solución es:")
    print(resolver("sodokudificil1.txt"))
    


#sol(a)