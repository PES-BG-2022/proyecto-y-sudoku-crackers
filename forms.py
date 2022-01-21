from shutil import unregister_unpack_format
from wtforms import Form
import numpy as np
from wtforms import IntegerField, StringField, FieldList, SubmitField, FormField

class B(Form):
    username=StringField("username")
    b1 = IntegerField("uno")
    b2 = IntegerField("dos")
    b3 = IntegerField("tres")
    b4 = IntegerField("4")
    b5 = IntegerField("5")
    b6 = IntegerField("6")
    b7 = IntegerField("7")
    b8 = IntegerField("8")
    b9 = IntegerField("9")

class A(Form):
    a1 = StringField("Ingrese su nombre: ")
    a2 = FieldList(FormField(B),min_entries = 9)
    s=SubmitField("Subir")

