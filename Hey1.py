from flask import Flask, render_template, request
from flask.scaffold import F


app = Flask(__name__)

subscribers = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/leermas')
def leermas():
    return render_template('leermas.html')

@app.route('/Pizza')
def Pizza():
    return render_template('Pizza.html')

@app.route('/pizza1')
def pizza1():
    return render_template('pizza1.html')

@app.route('/pizza2')
def pizza2():
    return render_template('pizza2.html')

@app.route('/pizza3')
def pizza3():
    return render_template('pizza3.html')

@app.route('/pizza4')
def pizza4():
    return render_template('pizza4.html')

@app.route('/suscribe')
def suscribe():
    return render_template('suscribe.html')

@app.route('/form', methods=["POST"])
def form():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    subscribers.append(f"{first_name} {last_name} {email}")
    return render_template('form.html', subscribers=subscribers)

if __name__ == "__main__":
    app.run(debug=True)

