from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/tlacu')
def tlac():
    return render_template("tlacu.html")

@app.route('/carac')
def carac():
    return render_template("carac.html")

@app.route('/dinosaurios')
def dinosaurios():
    return render_template("dinosaurios.html")

@app.route('/contacto')
def v2():
    return render_template("contacto.html")

@app.route('/index')
def v1():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
