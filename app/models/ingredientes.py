from sqlalchemy import Column, Integer, String, Date, Boolean, Numeric, DATE, ForeignKey, ForeignKeyConstraint
from app import db 

class Ingrediente(db.Model):
    __tablename__ = "ingredientes"

    id_ingrediente = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self,nome):
        self.nome = nome

    def __repr__(self):
        return '<Ingrediente %r>' % self.nome
