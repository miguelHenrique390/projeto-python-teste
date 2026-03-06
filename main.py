from flask import Flask 

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello World!!!</h1>"

@app.route("/curso")
def curso():
    return "<h1>Curso: Tecnico em Analise e Desenvolvimento de Sistemas</h1>"

if __name__ == "__main__":
    app.run()