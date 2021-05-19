from app import db
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import relationship, backref
ingredientes_receita = db.Table('ingredientes_receita',
    db.Column('id_ingrediente', db.Integer, db.ForeignKey('ingredientes.id_ingrediente')),
    db.Column('id_receita', db.Integer, db.ForeignKey('receitas.id_receita'))
    )
    
    

class Receita(db.Model):
    __tablename__ = "receitas"

    id_receita = db.Column(db.Integer, primary_key=True)
    nome_receita = db.Column(db.String(80), unique=True, nullable=False)
    tempo = db.Column(db.String(80))
    modo = db.Column(db.String(255))
    ingredientes = relationship("Ingrediente", secondary=ingredientes_receita, backref = db.backref('receitas'), lazy='dynamic', uselist=True)

    def __init__(self,nome_receita,tempo,modo):
        self.nome_receita= nome_receita
        self.tempo = tempo
        self.modo = modo
        
    def __repr__(self):
        return '<Receita %r>' % self.nome_receita