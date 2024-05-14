#Importar el módulo Flask en el proyecto.
from flask import Flask, render_template

#Crear un objeto de la clase Flask.
app = Flask(__name__)

#La función route() de la clase Flask.
@app.route("/")
def home():

    name = 'Daniela'
    age = '17'

    return render_template('index.html', name=name, age=age)

@app.route("/padre")
def padre():

    name = 'Eduardo'
    age = '45'

    return render_template('padre.html', name=name, age=age)

@app.route("/madre")
def madre():

    name = 'Erminia'
    age = '45'

    return render_template('madre.html', name=name, age=age)

@app.route("/primo")
def primo():

    name = 'Nathan'
    age = '3'

    return render_template('primo.html', name=name, age=age)

#Ejecutamos la app en el servidor local.
app.run()
