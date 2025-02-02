from flask import Flask, render_template, request, redirect, session, flash, url_for
from models.Product import Product

app = Flask(__name__)

listproduct = []


@app.route('/bancos')
def bancos():
    return render_template('index.html')


@app.route('/clientes')
def clientes():
    return render_template('index.html')


@app.route('/pedidos')
def pedidos():
    return render_template('index.html')


@app.route('/')
def relatorio():
    return render_template('index.html')


@app.route('/estoque')
def estoque():
    return render_template('index.html')


infos = [
    {'name': 'Nome', 'type': 'text'},
    {'name': 'Preço', 'type': 'number'},
    {'name': 'Tipo', 'type': 'text'},
]


@app.route('/produtos')
def produtos():

    return render_template('produtos.html', infos=infos, listproduct=listproduct)


@app.route('/registrar', methods=["POST",])
def registrar():
    nome = request.form['Nome']
    preco = request.form['Preço']
    tipo = request.form['Tipo']

    newProduct = Product(1, nome, preco, tipo)

    listproduct.append(newProduct)

    return redirect('/produtos')


@app.route('/usuarios')
def usuarios():
    return render_template('index.html')


app.run(debug=True)
