from sqlalchemy import Column, Integer, String, Date, Boolean, Numeric, DATE, ForeignKey, ForeignKeyConstraint
from app import db 

class Ingrediente(db.Model):
    __tablename__ = "receita_ingrediente"

    id_ingrediente = db.Column(db.Integer, primary_key=True)
    id_receita = db.Column(db.Integer, primary_key=True)