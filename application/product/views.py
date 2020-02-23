from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required
from application.product.models import Product
from application.product.forms import ProductForm
from application.row.models import Row

# Onko tuote käytössä jollain laskulla?
def deletable(number):
    return Row.query.filter_by(product_num=number).count() == 0

# Tuoteluettelo
@app.route("/products/", methods=["GET"])
def products_index():
    last = int((Product.query.count()-1)/5)+1
    last = last if last > 0 else 1
    page = request.args.get('page', default = 1, type = int)
    page = page if page >= 1 else 1
    page = page if page <= last else last
    products = Product.query.paginate(page=page, per_page=5, error_out=False).items
    return render_template("product/list.html", products=products, page=page, last=last)

# Muokkauslomake
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
        return render_template("product/edit.html", form=form, num=number, delete=deletable(number))
    else:
        return redirect(url_for("products_index"))

# Muokatun tuotteen tallennus
@app.route("/products/<int:number>/", methods=["POST"])
@login_required
def product_save(number):
    form = ProductForm(request.form)
    if not form.validate():
        return render_template("product/edit.html", form=form, num=number, delete=deletable(number))
    prod = Product.query.get(number)
    if bool(prod) and bool(form.name.data):
        prod.name = form.name.data
        prod.unit = form.unit.data
        prod.price = form.price.data
        prod.category = form.category.data
        db.session().commit()
    return redirect(url_for("products_index"))

# Uuden tuotteen luomislomake
@app.route("/products/new/", methods=["GET"])
@login_required
def product_form():
    return render_template("product/edit.html", form=ProductForm(), num=0, delete=False)

# Uuden tuotteen tallennus
@app.route("/products/", methods=["POST"])
@login_required
def product_create():
    form = ProductForm(request.form)
    if not form.validate():
        return render_template("product/edit.html", form = form, num=0, delete=False)
    prod = Product(form.name.data, form.unit.data, form.price.data, form.category.data)
    if bool(prod.name):
        db.session().add(prod)
        db.session().commit()
    return redirect(url_for("products_index"))

# Tuotteen poistaminen
@app.route("/products/del/<int:number>/", methods=["GET"])
@login_required
def product_delete(number):
    prod = Product.query.get(number)
    if bool(prod) and deletable(number):
        db.session().delete(prod)
        db.session().commit()
    return redirect(url_for("products_index"))
