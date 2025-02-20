from flask import Flask,render_template, request
import forms
from datetime import datetime
import Zodiaco


app=Flask(__name__)

@app.route("/")
def index():
    titulo="IDGS805"
    lista=["Pedro,juan,Mario"]
    return render_template("index.html",titulo=titulo,lista=lista)

@app.route("/ejemplo1")
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route("/ejemplo2")
def ejemplo2():
    return render_template("ejemplo2.html")


@app.route("/Hola")
def hola():
    return "<h1>Hola mundooo cris</h1>"


@app.route("/user/<string:user>")
def user(user):
    return f"hola,{user}"

@app.route("/numero/<int:n>")
def numero(n):
    return f"El numeri es: {n}"

@app.route("/user/<int:id>/<string:username>")
def username(id,username):
    return f"El usuario es: {username} con id: {id}"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return f"La suma es: {n1+n2}"

@app.route("/default/")
@app.route("/default/<string:tem>")
def func1(tem='Juan'):
    return f"Hola, {tem}"

@app.route("/form1")
def form1():
    return '''
            <form>
            <label for="nombre">Nombre:</label>
            </form>
    
           '''
           
           
           
@app.route("/OperasBas")
def operas():
    return render_template("OperasBas.html")

@app.route("/resultado", methods=["GET", "POST"])
def result():
    if request.method == "POST":
        try:
            num1 = int(request.form.get("n1"))
            num2 = int(request.form.get("n2"))
            resultado = num1 * num2
            return f"La multiplicación de {num1} x {num2} = {resultado}"
        except ValueError:
            return "Error: Asegúrate de ingresar números válidos."
    return "Usa el formulario para enviar los números."

    



@app.route("/alumnos", methods = ["GET", "POST"])
def alumnos():
    mat=""
    nom=""
    ape=""
    email=""
    alumno_clase=forms.UserForm(request.form)
    if request.method=="POST" and alumno_clase.validate():
        mat = alumno_clase.matricula.data
        nom = alumno_clase.nombre.data
        ape = alumno_clase.apellido.data
        email = alumno_clase.email.data
        print('Nombre: {}'.format(nom)) 
    return render_template("Alumnos.html", form=alumno_clase, mat=mat, nom=nom, ape=ape, email=email)



def calcular_edad(dia, mes, año):
    hoy = datetime.today()
    fecha_nacimiento = datetime(año, mes, dia)
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad

def signo_zodiaco_chino(año):
    signos = ["Mono", "Gallo", "Perro", "Cerdo", "Rata", "Buey", "Tigre", "Conejo", "Dragon", "Serpiente", "Caballo", "Cabra"]
    return signos[año % 12]  

@app.route("/zodiaco", methods=["GET", "POST"])
def zodiaco():
    nom = ""
    apeP = ""
    apeM = ""
    dia = ""
    mes = ""
    año = ""
    edad = None
    signo = ""
    sexo = ""
    imagen_signo = ""

    alumno_claseZ = Zodiaco.UserFormZ(request.form)
    if request.method == "POST" and alumno_claseZ.validate():
        nom = alumno_claseZ.nombre.data
        apeP = alumno_claseZ.apellidoP.data
        apeM = alumno_claseZ.apellidoM.data
        dia = int(alumno_claseZ.dia.data)
        mes = int(alumno_claseZ.mes.data)
        año = int(alumno_claseZ.año.data)
        sexo = "Masculino" if alumno_claseZ.sexo.data == "M" else "Femenino"

        edad = calcular_edad(dia, mes, año)
        signo = signo_zodiaco_chino(año)
        imagen_signo = f"../static/bootstrap/img/{signo.lower()}.jpg"

    return render_template("Zodiaco.html", form=alumno_claseZ, nom=nom, apeP=apeP, apeM=apeM, dia=dia, mes=mes, año=año, edad=edad, signo=signo, imagen_signo=imagen_signo, sexo=sexo)
  
    



@app.route("/Cinepolis")
def Cine1():
    return render_template("Cinepolis.html")
 
def calcularBoletos(numP):
    return numP * 7

def calcularDescuento2(numB):
    return numB * 12

def calcularDescuento5(numB):
    return (numB * 12) * 0.9  

def calcularDescuentoMAS5(numB):
    return (numB * 12) * 0.85  

def aplicarDescuentoTarjeta(total):
    return total * 0.9  #

@app.route("/Cinepolis2", methods=["GET", "POST"])
def Cine():
    total = None
    mensaje = ""
    if request.method == "POST":
        try:
            nombre = request.form["nombre"]
            numP = int(request.form["cantidad_personas"])
            numB = int(request.form["cantidad_boletos"])
            tarjetaCINECO = request.form.get("cineco") == "si"
            boletosPermitidos = calcularBoletos(numP)
            if numB > boletosPermitidos:
                mensaje = f"No puedes comprar más de {boletosPermitidos} boletos."
            else:
                if numB <= 2:
                    total = calcularDescuento2(numB)
                elif numB <= 5:
                    total = calcularDescuento5(numB)
                else:
                    total = calcularDescuentoMAS5(numB)

                if tarjetaCINECO:
                    total = aplicarDescuentoTarjeta(total)
                total = f"${total:.2f}"
        except ValueError:
            mensaje = "Por favor, ingresa valores válidos."
    return render_template("Cinepolis.html", total=total, mensaje=mensaje)






if __name__=="__main__":
    app.run(debug=True,port=3000)


