from sqlalchemy import Column, Integer, String, Date, Boolean, Numeric, DATE, ForeignKey, ForeignKeyConstraint
from app import db 
from sqlalchemy.orm import relationship, backref

class ReceitaIngrediente(db.Model):
    __tablename__ = "receita_ingrediente"

    id_ingrediente = db.Column(db.Integer, ForeignKey('ingredientes.id_ingrediente'), primary_key=True)
    id_receita = db.Column(db.Integer, ForeignKey('receitas.id_receita'),primary_key=True)
    quantidade = db.Column('quantidade', db.String(80))
    receita = relationship("Receita", backref="ingredient")
    ingredientes = relationship("Ingrediente", backref="receit")

    def __init__(self,quantidade):
        self.quantidade = quantidade
