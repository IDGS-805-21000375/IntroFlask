from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, RadioField, IntegerField, EmailField
from wtforms import validators

class UserFormZ(Form):
    nombre = StringField("Nombre", [
        validators.DataRequired(message="El campo es requerido")
    ])
    
    apellidoP = EmailField("Apellido Paterno", [
        validators.DataRequired(message="El campo es requerido")
    ])
    
    apellidoM = EmailField("Apellido Materno", [
        validators.DataRequired(message="El campo es requerido")
    ])
    
    dia = StringField("Día", [
        validators.DataRequired(message="El campo es requerido")
    ])
     
    mes = StringField("Mes", [
        validators.DataRequired(message="El campo es requerido")
    ])
      
    año = StringField("Año", [
        validators.DataRequired(message="El campo es requerido")
    ])
    
    sexo = RadioField("Sexo", choices=[('M', 'Masculino'), ('F', 'Femenino')], 
                      default='M', validators=[validators.DataRequired()])
