import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)

engine = create_engine('sqlite:///db.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Aluno(Base):
    __tablename__ = 'alunos'


    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    endereco = Column(String)


    def __init__(self, name, email, endereco):
        self.name = name
        self.email = email
        self.endereco = endereco



@app.route('/aluno', methods=['GET', 'POST'])
def aluno():
    try:
        if request.method == 'POST':
            nome = request.form['name']
            email = request.form['email']
            endereco = request.form['endereco']
            aluno = Aluno(nome,email,endereco)
            session.add(aluno)
            session.commit()
    except Exception as error:
        print('Problema de inserção no banco de dados: '+ str(error))
    finally:
        return render_template('aluno.html')


@app.route('/show_aluno', methods=['GET'])
def show_aluno():
    data = session.query(Aluno).all()
    for item in data:
        print(item.id,item.name)
    return render_template('show_aluno.html',data=data)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
