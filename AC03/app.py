import os
from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from config import BaseConfig

app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)

from models import *

@app.route('/')
def inicio():
    return render_template('produto.html')

@app.route('/produto', methods=['POST'])
def post_produto():
    produto = request.form.get('produto')
    categoria = request.form.get('categoria')
    preco = request.form.get('preco')
    if produto and categoria and preco:
        produtos = Produtos(produto, categoria, preco)
        db.session.add(produtos)
        db.session.commit()
        db.session.flush()
        url = f"/lista/produto/{produtos.id}"
        return redirect(url, code=302)
    return render_template('show_produtos.html')

@app.route('/lista/produto/<int:nid>', methods=['GET'])
def show_produto(nid):
    produtos = Produtos.query.filter_by(id=nid).all()
    db.session.commit()
    return render_template('show_produtos.html', produtos=produtos)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5050))
    app.run(host='0.0.0.0', port=port)
