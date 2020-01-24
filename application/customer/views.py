from application import app, db
from flask import redirect, render_template, request, url_for
from application.customer.models import Customer


@app.route("/customers/", methods=["GET"])
def customers_index():
    return render_template("customer/list.html", customers=Customer.query.all())


@app.route("/customers/<int:number>/", methods=["GET"])
def customer_edit(number):
    c = Customer.query.get(number)
    if bool(c):
        return render_template("customer/edit.html", customer=c)
    else:
        return redirect(url_for("customers_index"))


@app.route("/customers/<int:number>/", methods=["POST"])
def customer_save(number):
    c = Customer.query.get(number)
    if bool(c) and bool(request.form.get("name")):
        c.name = request.form.get("name")
        c.address = request.form.get("address")
        db.session().commit()
    return redirect(url_for("customers_index"))


@app.route("/customers/new/", methods=["GET"])
def customer_form():
    empty = Customer("", "")
    empty.number = 0
    return render_template("customer/edit.html", customer=empty)


@app.route("/customers/", methods=["POST"])
def customer_create():
    c = Customer(request.form.get("name"), request.form.get("address"))
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
