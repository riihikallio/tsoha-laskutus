from application import app, db
from flask import redirect, render_template, request, url_for
from application.customer.models import Customer
from application.customer.forms import CustomerForm


@app.route("/customers/", methods=["GET"])
def customers_index():
    return render_template("customer/list.html", customers=Customer.query.all())


@app.route("/customers/<int:number>/", methods=["GET"])
def customer_edit(number):
    c = Customer.query.get(number)
    f = CustomerForm()
    f.name.data = c.name
    f.address.data = c.address
    if bool(c):
        return render_template("customer/edit.html", form=f, num=c.number)
    else:
        return redirect(url_for("customers_index"))


@app.route("/customers/<int:number>/", methods=["POST"])
def customer_save(number):
    f = CustomerForm(request.form)
    c = Customer.query.get(number)
    if bool(c) and bool(f.name.data):
        c.name = f.name.data
        c.address = f.address.data
        db.session().commit()
    return redirect(url_for("customers_index"))


@app.route("/customers/new/", methods=["GET"])
def customer_form():
    return render_template("customer/edit.html", form=CustomerForm(), num=0)


@app.route("/customers/", methods=["POST"])
def customer_create():
    f = CustomerForm(request.form)
    c = Customer(f.name.data, f.address.data)
    if bool(c.name):
        db.session().add(c)
        db.session().commit()
    return redirect(url_for("customers_index"))


@app.route("/customers/del/<int:number>/", methods=["GET"])
def customer_delete(number):
    c = Customer.query.get(number)
    if bool(c):
        db.session().delete(c)
        db.session().commit()
    return redirect(url_for("customers_index"))
