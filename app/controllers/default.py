from flask import render_template, request, url_for, redirect, Flask
from app import app
from app import db

from app.models.ingredientes import Ingrediente
from app.models.receitas import Receita
from app.models.receita_ingrediente import ReceitaIngrediente

@app.route('/')
def index():
    receitas = Receita.query.all()
    ingredientes = Ingrediente.query.all()
    return render_template('index.html', 
                            receitas=receitas, ingredientes=ingredientes)

@app.route('/cadastro/ingrediente', methods = ['GET', 'POST'])
def cadastro_ingrediente():
    receita = Receita.query.all()
    ingredientes = Ingrediente.query.all()
    if request.method == 'POST':
        nome = (request.form.get("nome"))
        if nome:
            i = Ingrediente(nome)
            db.session.add(i)
            db.session.commit()
            return redirect(url_for('cadastro_ingrediente'))
    return render_template('cadastro_ingredientes.html', ingredientes=ingredientes, receita=receita)                          

@app.route('/cadastro/receita',  methods = ['GET', 'POST'])
def cadastro_receita():
    ingredientes = Ingrediente.query.all()
    igs = []
    if request.method == 'POST':
        igs = (request.form.getlist("igs"))
        qtds = (request.form.getlist("qtd"))
        qtds = [x for x in qtds if x]
        nome_receita = (request.form.get("nome_receita"))
        tempo = (request.form.get("tempo"))
        modo = (request.form.get("modo"))
        if nome_receita:
            r = Receita(nome_receita,tempo,modo)
            for id,qtd in zip(igs,qtds):
                ri = ReceitaIngrediente (qtd)
                ri.ingredientes = Ingrediente.query.get(id)            
                r.ingredientes.append(ri)
            db.session.add(r)
            db.session.commit()
    return render_template('cadastro_receitas.html',ingredientes=ingredientes)

@app.route('/delete/receita/<int:id>')
def delete_receita(id):
    receita = Receita.query.get(id)
    ri = ReceitaIngrediente.query.filter_by(id_receita=id).delete(synchronize_session='fetch')
    db.session.delete(receita)
    db.session.commit()
    return redirect(url_for('index'))    

@app.route('/delete/ingrediente/<int:id>')
def delete(id):
    ingrediente = Ingrediente.query.get(id)
    ri = ReceitaIngrediente.query.filter_by(id_ingrediente = id).all()
    if not ri:
        db.session.delete(ingrediente)
        db.session.commit()
        return redirect(url_for('cadastro_ingrediente'))
    else: 
        print('Receitas possuem esse ingrediente, não é possível realizar a exclusão')
    return redirect(url_for('index'))   

@app.route('/edit/ingrediente/<int:id>', methods = ['GET', 'POST'])
def edit(id):
    ingrediente = Ingrediente.query.get(id)
    if request.method == 'POST':
        ingrediente.nome = request.form['nome_']
        db.session.commit()
        return redirect(url_for('cadastro_ingrediente'))
    return render_template('cadastro_ingredientes.html', ingrediente=ingrediente)

@app.route('/edit/receita/<int:id>', methods = ['GET', 'POST'])
def edit_receita(id):
    receita = Receita.query.get(id)
    if request.method == 'POST':
        receita.nome_receita = request.form['_nome']
        receita.tempo = (request.form.get("_tempo"))
        receita.modo = (request.form.get("_modo"))
        igs = (request.form.getlist("_igs"))
        qtds = (request.form.getlist("_qtd"))
        qtds = [x for x in qtds if x]
        for ig,qtd in zip(igs,qtds):
            ri = ReceitaIngrediente.query.filter_by(id_receita=id,id_ingrediente = ig).update(dict(quantidade = qtd))
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('index.html', ingrediente=ingrediente) 

@app.route('/receita/<int:id>')
def receita(id):
    receita = Receita.query.get(id)
    ingrediente = Ingrediente.query.all()
    return render_template('receita.html', receita=receita, ingrediente=ingrediente)