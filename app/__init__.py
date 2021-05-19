from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///livro.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/livros'
db = SQLAlchemy(app)
from app.models.ingredientes import Ingrediente
from app.models.receitas import Receita
db.create_all()

app.debug = True    
from app.controllers import default