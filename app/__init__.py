from flask import Flask, render_template, request, redirect, session, flash, url_for
from models.Product import Product
from models.User import User
from models.Client import Client
from models.Purchase import Purchase

app = Flask(__name__)

app.jinja_env.globals.update(getattr=getattr)

listproduct = []
listusers = []
listclients = []
listpurchase = []


@app.route('/bancos')
def bancos():
    return render_template('index.html')


@app.route('/pedidos')
def pedidos():
    return render_template('index.html')


@app.route('/')
def relatorio():
    return render_template('index.html')


infosproducts = [
    {'name': 'Nome', 'type': 'text', 'obj': 'product'},
    {'name': 'Preço', 'type': 'number', 'obj': 'product'},
    {'name': 'Tipo', 'type': 'text', 'obj': 'product'},
]

infosusers = [
    {'name': 'Nome', 'type': 'text', 'obj': 'user'},
    {'name': 'Tipo', 'type': 'text', 'obj': 'user'},
]

infosclient = [
    {'name': 'Nome', 'type': 'text', 'obj': 'client'}
]

infospurchase = [
    {'name': 'Produto', 'type': 'text', 'obj': 'purchase'},
    {'name': 'Quantidade', 'type': 'number', 'obj': 'purchase'},
    {'name': 'Data', 'type': 'text', 'obj': 'purchase'},
    {'name': 'Valor', 'type': 'number', 'obj': 'purchase'},
]


@app.route('/produtos')
def produtos():

    return render_template('produtos.html', infos=infosproducts, list=listproduct)


@app.route('/usuarios')
def usuarios():

    return render_template('produtos.html', infos=infosusers, list=listusers)


@app.route('/clientes')
def clientes():
    return render_template('produtos.html', infos=infosclient, list=listclients)


@app.route('/estoque')
def estoque():
    return render_template('produtos.html', infos=infospurchase, list=listpurchase)


@app.route('/deletar/<obj>/<name>')
def deletar(obj, name):

    global listproduct
    global listusers
    global listclients
    global listpurchase

    if (obj == "product"):
        listproduct = list(
            filter(lambda product: product.product_name !=
                   name, listproduct)


        )
        return redirect('/produtos')

    elif (obj == "user"):
        listusers = list(
            filter(lambda user: user.user_name !=
                   name, listusers)
        )

        return redirect('/usuarios')

    elif (obj == "client"):
        listclients = list(
            filter(lambda client: client.client_name !=
                   name, listclients)

        )
        return redirect('/clientes')

    elif (obj == "purchase"):
        return redirect('/estoque')


@app.route('/registrar', methods=["POST",])
def registrar():

    obj = request.form.get('obj')
    nome = request.form.get('Nome')
    price = request.form.get('Preço')
    tipo = request.form.get('Tipo')
    product = request.form.get('Produto')
    quantity = request.form.get('Quantidade')
    value = request.form.get('Valor')
    date = request.form.get('Data')

    if (obj == "product"):

        newItem = Product(1, nome, price, tipo)
        listproduct.append(newItem)
        return redirect('/produtos')

    elif (obj == "user"):

        newItem = User(1, nome, tipo)
        listusers.append(newItem)
        return redirect('/usuarios')

    elif (obj == "client"):

        newItem = Client(1, nome)
        listclients.append(newItem)
        return redirect('/clientes')

    elif (obj == "purchase"):

        newItem = Purchase(1, quantity, date, value, product)
        listpurchase.append(newItem)
        return redirect('/estoque')


app.run(debug=True)
