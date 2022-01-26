from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key= "estoessecreto"
listaUsuarios=[]

#Rutas
@app.route("/", methods=["GET"])
def despliegaRegistroLogin():
    return render_template('index.html')

@app.route("/dashboard", methods=["GET"])
def despliegaDashboard():
    if 'nombre' in session:
        return render_template("dashboard.html", usuarios=listaUsuarios)
    else:
        return redirect("/")


@app.route("/registroUsuario", methods=["POST"])
def registrarUsuario():
    nuevoUsuario={
        "nombre":request.form["nombre"],
        "apellido":request.form["apellido"],
        "identificador":request.form["usuario"],
        "password":request.form["password"]
    }
    session["nombre"]=request.form["nombre"]
    session["apellido"]=request.form["apellido"]
    listaUsuarios.append(nuevoUsuario)
    return redirect( '/dashboard')

@app.route('/login',methods=["POST"])
def loginUsuario():
    nombreUsuario = request.form["usuarioLogin"]
    passwordUsuario = request.form["passwordLogin"]

    print( request.form )
    for usuario in listaUsuarios:
        if usuario["identificador"] == nombreUsuario and usuario["password"]==passwordUsuario:
            session["nombre"]=usuario["nombre"]
            session["apellido"]=usuario["apellido"]
            return redirect("/dashboard")
    return redirect( '/' )

@app.route("/logout", methods=["GET"])
def logoutUsuario():
    session.clear()
    return redirect(" / ")

if(__name__=="__main__"): 
    app.run(debug=True)