from flask import Flask
from flask import request
from flask import render_template
import numpy as np
import sudoku as sud
import forms 

app = Flask(__name__)


@app.route('/')#, methods=['GET','POST'])
def index():
    #sudoku_form = forms.sudokuform(request.form)
    form = forms.A()
    # if request.method == 'POST':
    #     print(A_form.a2.)
    #sudoku_form=form.sudokuform
    return render_template("index.html", nombre = name, edad = age, sudoku = sudoku, solucion = solucion,form = form)

@app.route("/r",methods = ['POST'])
def r():
    a=request.form["a1"]
    b=request.form
    br = { x:b[x] for x in b if "a2-" in x }
    print(br)
    return render_template("result.html", a = a, b=br)
 
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