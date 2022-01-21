from flask import Flask
from flask import request
from flask import render_template
import numpy as np
import sudoku as sud
import forms 

app = Flask(__name__)

@app.route('/')#, methods=['GET','POST'])
def index():
    form = forms.A()
    return render_template("index.html", sudoku = sudoku, solucion = solucion,form = form)

@app.route("/r",methods = ['POST'])
def r():
    a=request.form["a1"]
    b=request.form
    br = { x:b[x] for x in b if "a2-" in x }
    
    print(br)
    br_list = []
    contador = 0
    for x in br:
        br_list.append(br[x])
        print(br[x])
        contador+=1
    print(br_list)
    print(len(br_list))

    #QUEDA PENDIENTE TERMINAR CON ESTE LISTADO PARA CORROBORAR SOLUCION

    return render_template("result.html",  b=br, sudoku = sudoku, solucion = solucion, a=a)

if __name__ == '__main__':
    #AQUI SE SELECCIONA QUE SUDOKU RESOLVER
    sudoku   = sud.get_sudoku("sudoku3.txt") 
    solucion = sud.get_solucion("sudoku3.txt")
    app.run(debug=True)