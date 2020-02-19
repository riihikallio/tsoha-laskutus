from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required
from application.product.models import Product
from application.product.forms import ProductForm


@app.route("/products/", methods=["GET"])
def products_index():
    return render_template("product/list.html", products=Product.query.all())


@app.route("/products/<int:number>/", methods=["GET"])
@login_required
def product_edit(number):
    prod = Product.query.get(number)
    form = ProductForm()
    form.name.data = prod.name
    form.unit.data = prod.unit
    form.price.data = prod.price
    form.category.data = prod.category
    if bool(prod):
        return render_template("product/edit.html", form=form, num=prod.number)
    else:
        return redirect(url_for("products_index"))


@app.route("/products/<int:number>/", methods=["POST"])
@login_required
def product_save(number):
    form = ProductForm(request.form)
    if not form.validate():
        return render_template("product/edit.html", form=form, num=number)
    prod = Product.query.get(number)
    if bool(prod) and bool(form.name.data):
        prod.name = form.name.data
        prod.unit = form.unit.data
        prod.price = form.price.data
        prod.category = form.category.data
        db.session().commit()
    return redirect(url_for("products_index"))


@app.route("/products/new/", methods=["GET"])
@login_required
def product_form():
    return render_template("product/edit.html", form=ProductForm(), num=0)


@app.route("/products/", methods=["POST"])
@login_required
def product_create():
    form = ProductForm(request.form)
    if not form.validate():
        return render_template("product/edit.html", form = form, num=0)
    prod = Product(form.name.data, form.unit.data, form.price.data, form.category.data)
    if bool(prod.name):
        db.session().add(prod)
        db.session().commit()
    return redirect(url_for("products_index"))


@app.route("/products/del/<int:number>/", methods=["GET"])
@login_required
def product_delete(number):
    prod = Product.query.get(number)
    if bool(prod):
        db.session().delete(prod)
        db.session().commit()
    return redirect(url_for("products_index"))
