from flask import Flask
from flask import request
from flask import render_template
import numpy as np
import sudoku as sud
import form

app = Flask(__name__)


@app.route('/')
def index():
    #sudoku_form=form.sudokuform
    return render_template("index.html", nombre = name, edad = age, sudoku = sudoku, solucion = solucion)#, form = sudoku_form)

 
#funciona con esta URL: http://127.0.0.1:5000/params?params1=Juan_Manuel&params2=Jimenez_Cruz
#?params=1
#@app.route('/params')
#def saluda():
#    param1 = request.args.get("params1","no contiene este parametro")
#    param2 = request.args.get("params2","no contiene este parametro")
#    return f"El parametro es {param1} {param2}"


if __name__ == '__main__':
    name = "Juan Manuel"
    age = 25

    sudoku   = sud.get_sudoku("sudoku3.txt")
    solucion = sud.get_solucion("sudoku3.txt")
    app.run(debug=True)