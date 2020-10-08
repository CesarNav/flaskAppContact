# Esto importa la clase FLask que nos permite hacer nuevas instancias de flask
from flask import Flask

# Esto nos permite instancia la primera clase de FLask en una variable llamada app, __name__ se refiere al nombre del archivo principal
app = Flask(__name__)


if __name__ == '__main__':
    app.run( port = 8000, debug = True )

# Esto es un decorador de python, nos permite indicar que el programa se correrá en la raiz del proyecto.
@app.route('/')

# Este es la primer funcion que se ejecutará en el servidor
def hello():
    return 'Hello word Flask'