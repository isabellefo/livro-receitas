from app import db
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import relationship, backref
    

class Receita(db.Model):
    __tablename__ = "receitas"

    id_receita = db.Column(db.Integer, primary_key=True)
    nome_receita = db.Column(db.String(80), unique=True, nullable=False)
    tempo = db.Column(db.String(80))
    modo = db.Column(db.Text)
    ingredientes = relationship("ReceitaIngrediente", backref="receit")

    def __init__(self,nome_receita,tempo,modo):
        self.nome_receita= nome_receita
        self.tempo = tempo
        self.modo = modo
        
    def __repr__(self):
        return '<Receita %r>' % self.nome_receita