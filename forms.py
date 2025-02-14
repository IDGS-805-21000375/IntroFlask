from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,FieldList,RadioField,EmailField

class UserForm(Form):
    matricula=StringField('Matricula')
    nombre=StringField('Nombre')
    apellido=StringField('Apellido')
    matricula=StringField('Matricula')
    email=EmailField('Correo')
    