from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

# Criar um API flask
app = Flask(__name__)

# Configurações
app.config['SECRET_KEY'] = '*********'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

# Instância do SQLAlchemy
db = SQLAlchemy(app)

# Definir a estrutura da tabela Postagem
class Postagem(db.Model):
    __tablename__ = 'postagem'
    id_postagem = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String)
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor'))

# Definir a estrutura da tabela Autor
class Autor(db.Model):
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)  # Senha em texto claro (mas será criptografada)
    admin = db.Column(db.Boolean)
    postagens = db.relationship('Postagem', backref='autor', lazy=True)

# Criar o banco de dados e adicionar um usuário dentro do contexto da aplicação Flask
with app.app_context():
    db.drop_all()
    db.create_all()

    # Criar usuário administrador com senha criptografada
    senha_hash = generate_password_hash('*********')  # Criptografando a senha
    autor = Autor(nome='******', email='*********', senha=senha_hash, admin=True)
    db.session.add(autor)
    db.session.commit()
