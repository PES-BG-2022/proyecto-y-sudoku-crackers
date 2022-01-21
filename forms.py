from shutil import unregister_unpack_format
from wtforms import Form
import numpy as np
from wtforms import IntegerField, StringField, FieldList, SubmitField, FormField
class B(Form):
    username=StringField("username")
    b1 = StringField("uno")
    b2 = StringField("dos")
    b3 = StringField("tres")

class A(Form):
    a1 = StringField("Texto")
    a2 = FieldList(FormField(B),min_entries = 9)
    s=SubmitField("Subir")

