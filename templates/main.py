from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
agenda=[]
consulta=[]
# Configura la conexión a la base de datos MySQL con pymysql
@app.route('/')
def form():
    return render_template('index.html')

@app.route('/contactanos', methods=['POST'])
def contactenos():
    nombre = request.form.get('full_name')
    email = request.form.get('email')
    consultas = request.form.get('user_message')
    if nombre and email:
       agenda.append({'Nombre completo': nombre, 'Email': email})
       consulta.append(consultas)
    return render_template('index.html')

@app.route('/agricola')
def form():
    return render_template('agricola.html')

@app.route('/construccion')
def form():
    return render_template('construccion.html')

@app.route('/energia')
def form():
    return render_template('energia.html')

@app.route('/mineria')
def form():
    return render_template('mineria.html')

@app.route('/otros')
def form():
    return render_template('otros.html')

@app.route('/soluciones')
def form():
    return render_template('soluciones.html')

if __name__ == '__main__':
    app.run(debug=True)