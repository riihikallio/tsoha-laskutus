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
    p = Product.query.get(number)
    f = ProductForm()
    f.name.data = p.name
    f.unit.data = p.unit
    f.price.data = p.price
    if bool(p):
        return render_template("product/edit.html", form=f, num=p.number)
    else:
        return redirect(url_for("products_index"))


@app.route("/products/<int:number>/", methods=["POST"])
@login_required
def product_save(number):
    f = ProductForm(request.form)
    if not f.validate():
        return render_template("product/edit.html", form=f, num=number)
    p = Product.query.get(number)
    if bool(p) and bool(f.name.data):
        p.name = f.name.data
        p.unit = f.unit.data
        p.price = f.price.data
        db.session().commit()
    return redirect(url_for("products_index"))


@app.route("/products/new/", methods=["GET"])
@login_required
def product_form():
    return render_template("product/edit.html", form=ProductForm(), num=0)


@app.route("/products/", methods=["POST"])
@login_required
def product_create():
    f = ProductForm(request.form)
    if not f.validate():
        return render_template("product/edit.html", form = f, num=0)
    p = Product(f.name.data, f.unit.data, f.price.data)
    if bool(p.name):
        db.session().add(p)
        db.session().commit()
    return redirect(url_for("products_index"))


@app.route("/products/del/<int:number>/", methods=["GET"])
@login_required
def product_delete(number):
    p = Product.query.get(number)
    if bool(p):
        db.session().delete(p)
        db.session().commit()
    return redirect(url_for("products_index"))
