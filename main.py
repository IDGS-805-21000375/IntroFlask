from flask import Flask,render_template, request

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
            num1 = int(request.form.get("n1", 0))
            num2 = int(request.form.get("n2", 0))
            resultado = num1 * num2
            return f"La multiplicación de {num1} x {num2} = {resultado}"
        except ValueError:
            return "Error: Asegúrate de ingresar números válidos."
    return "Usa el formulario para enviar los números."

    
    
    
    
    
@app.route("/Cinepolis")
def Cine1():
    return render_template("Cinepolis.html")
 
def calcularBoletos(numP):
    return numP * 7

def calcularDescuento2(numB):
    return numB * 12

def calcularDescuento5(numB):
    return (numB * 12) * 0.9  # 10% de descuento

def calcularDescuentoMAS5(numB):
    return (numB * 12) * 0.85  # 15% de descuento

def aplicarDescuentoTarjeta(total):
    return total * 0.9  # 10% de descuento adicional

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


