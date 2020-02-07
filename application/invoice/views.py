from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required
from application.invoice.models import Invoice
from application.invoice.forms import InvoiceForm


@app.route("/invoices/", methods=["GET"])
@login_required
def invoices_index():
    return render_template("invoice/list.html", invoices=Invoice.query.all())


@app.route("/invoices/<int:number>/", methods=["GET"])
@login_required
def invoice_show(number):
    i = Invoice.query.get(number)
    f = InvoiceForm()
    f.name.data = p.name
    f.unit.data = p.unit
    f.price.data = p.price
    f.category.data = p.category
    if bool(i):
        return render_template("invoice/edit.html", form=f, num=p.number)
    else:
        return redirect(url_for("invoices_index"))

@app.route("/invoices/<int:number>/edit/", methods=["GET"])
@login_required
def invoice_edit(number):
    i = Invoice.query.get(number)
    f = InvoiceForm()
    f.name.data = p.name
    f.unit.data = p.unit
    f.price.data = p.price
    f.category.data = p.category
    if bool(i):
        return render_template("invoice/edit.html", form=f, num=p.number)
    else:
        return redirect(url_for("invoices_index"))


@app.route("/invoices/<int:number>/", methods=["POST"])
@login_required
def invoice_save(number):
    f = InvoiceForm(request.form)
    if not f.validate():
        return render_template("invoice/edit.html", form=f, num=number)
    i = Invoice.query.get(number)
    if bool(i) and bool(f.name.data):
        i.name = f.name.data
        i.unit = f.unit.data
        i.price = f.price.data
        i.category = f.category.data
        i.account_id = current_user.id
        db.session().commit()
    return redirect(url_for("invoices_index"))


@app.route("/invoices/new/", methods=["GET"])
@login_required
def invoice_form():
    return render_template("invoice/edit.html", form=InvoiceForm(), num=0)


@app.route("/invoices/", methods=["POST"])
@login_required
def invoice_create():
    f = InvoiceForm(request.form)
    if not f.validate():
        return render_template("invoice/edit.html", form = f, num=0)
    i = Invoice(f.name.data, f.unit.data, f.price.data, f.category.data)
    if bool(i.name):
        db.session().add(i)
        db.session().commit()
    return redirect(url_for("invoices_index"))


@app.route("/invoices/del/<int:number>/", methods=["GET"])
@login_required
def invoice_delete(number):
    i = Invoice.query.get(number)
    if bool(p):
        db.session().delete(i)
        db.session().commit()
    return redirect(url_for("invoices_index"))
