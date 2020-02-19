from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required
from application.customer.models import Customer
from application.customer.forms import CustomerForm


@app.route("/customers/", methods=["GET"])
@login_required
def customers_index():
    return render_template("customer/list.html", customers=Customer.query.all())


@app.route("/customers/<int:number>/", methods=["GET"])
@login_required
def customer_edit(number):
    cust = Customer.query.get(number)
    form = CustomerForm()
    form.name.data = cust.name
    form.address.data = cust.address
    if bool(cust):
        return render_template("customer/edit.html", form=form, num=cust.number)
    else:
        return redirect(url_for("customers_index"))


@app.route("/customers/<int:number>/", methods=["POST"])
@login_required
def customer_save(number):
    form = CustomerForm(request.form)
    if not form.validate():
        return render_template("customer/edit.html", form = form, num=number)
    cust = Customer.query.get(number)
    if bool(cust) and bool(form.name.data):
        cust.name = form.name.data
        cust.address = form.address.data
        db.session().commit()
    return redirect(url_for("customers_index"))


@app.route("/customers/new/", methods=["GET"])
@login_required
def customer_form():
    return render_template("customer/edit.html", form=CustomerForm(), num=0)


@app.route("/customers/", methods=["POST"])
@login_required
def customer_create():
    form = CustomerForm(request.form)
    if not form.validate():
        return render_template("customer/edit.html", form = form, num=0)
    cust = Customer(form.name.data, form.address.data)
    if bool(cust.name):
        db.session().add(cust)
        db.session().commit()
    return redirect(url_for("customers_index"))


@app.route("/customers/del/<int:number>/", methods=["GET"])
@login_required
def customer_delete(number):
    cust = Customer.query.get(number)
    if bool(cust):
        db.session().delete(cust)
        db.session().commit()
    return redirect(url_for("customers_index"))
