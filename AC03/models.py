from app import db

class Produtos(db.Model):
    __tablename__ = "produtos"

    id = db.Column(db.Integer, primary_key=True)
    produto = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.String(100), nullable=False)

    def __init__(self, produto, categoria, preco):
        self.produto = produto
        self.categoria = categoria
        self.preco = preco
