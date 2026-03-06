from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello World!!!</h1>"

@app.route("/curso")
def curso():
    return "<h1>Curso: Tecnico em Analise e Desenvolvimento de Sistemas</h1>"

@app.route("/cidade")
def cidade():
    cidade = {
        "nome": "piracicaba",
        "idade": 258,
        "estado": "SP",
        "habitantes": 400000

    }
    return cidade

@app.route("/musicas")
def musicas():
    favoritas = ["kiss of life", "metamorphosis", "black", "blinding lights", "even flow", "ballin", "A barca"]
    return favoritas

@app.route("/cardapio")
def cardapio():
    return render_template("cardapio.html")

if __name__ == "__main__":
    app.run(debug=True)