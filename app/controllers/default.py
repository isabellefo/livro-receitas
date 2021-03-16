from flask import render_template
from app import app


@app.route('/index/<user>')
@app.route('/', defaults={'user':None})
def index(user):
    return render_template('index.html', 
                            user=user)

@app.route('/cadastro/ingrediente')
def cadastro_ingrediente():
    return render_template('cadastro_ingredientes.html')                            

@app.route('/cadastro/receita')
def cadastro_receita():
    return render_template('cadastro_receitas.html')