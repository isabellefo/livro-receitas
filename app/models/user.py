from app import db 

class Ingrediente(db.Model):
    __tablename__ = "user"

    id_user = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(80), unique=True, nullable=False)
    senha = db.Column(db.String(80), nullable=False)

    def __init__(self,user):
        self.user = user

    def __repr__(self):
        return '<Ingrediente %r>' % self.nome