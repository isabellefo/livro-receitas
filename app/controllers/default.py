from flask import render_template, request, url_for, redirect, Flask
from app import app
from app import db

from app.models.ingredientes import Ingrediente
from app.models.receitas import Receita


@app.route('/index/<user>')
@app.route('/', defaults={'user':None})
def index(user):
    receitas = Receita.query.all()
    return render_template('index.html', 
                            user=user)

@app.route('/cadastro/ingrediente', methods = ['GET', 'POST'])
def cadastro_ingrediente():
    if request.method == 'POST':
        nome = (request.form.get("nome"))
        if nome:
            i = Ingrediente(nome)
            db.session.add(i)
            db.session.commit()
    ingredientes = Ingrediente.query.all()
    return render_template('cadastro_ingredientes.html', ingredientes=ingredientes)                            

@app.route('/cadastro/receita',  methods = ['GET', 'POST'])
def cadastro_receita():
    if request.method == 'POST':
        nome_receita = (request.form.get("nome_receita"))
        tempo = (request.form.get("tempo"))
        modo = (request.form.get("modo"))
        if nome_receita:
            r = Receita(nome_receita,tempo,modo)
            db.session.add(r)
            db.session.commit()
    return render_template('cadastro_receitas.html')

@app.route('/delete/ingrediente/<int:id>')
def delete(id):
    ingrediente = Ingrediente.query.get(id)
    db.session.delete(ingrediente)
    db.session.commit()
    return render_template('cadastro_ingredientes.html')

@app.route('/edit/ingrediente/<int:id>', methods = ['GET', 'POST'])
def edit(id):
    ingrediente = Ingrediente.query.get(id)
    if request.method == 'POST':
        ingrediente.nome = request.form['nome_']
        db.session.commit()
        return redirect(url_for('cadastro_ingrediente'))
    return render_template('cadastro_ingredientes.html', ingrediente=ingrediente) 

@app.route('/receita')
def receita():
    return render_template('receita.html')