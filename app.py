from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/nao")
def nao():
    return render_template("nao.html")

@app.route("/sim")
def sim():
    return render_template("sim.html")

if __name__ == "__main__":
    app.run(debug=True)
