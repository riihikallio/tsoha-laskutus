from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.invoice.models import Invoice, Row
from application.invoice.forms import InvoiceForm, RowForm


@app.route("/invoices/", methods=["GET"])
@login_required
def invoices_index():
    return render_template("invoice/list.html", invoices=Invoice.query.all())


@app.route("/invoices/<int:number>/", methods=["GET"])
@login_required
def invoice_show(number):
    i = Invoice.query.get(number)
    f = InvoiceForm()
    f.customer.data = i.customer
    for r in i.rows:
        print("********************")
        print(type(r))
        rdata = RowForm()
        rdata.product.data = r.product
        rdata.count.data = r.count
        f.rows.data.append(rdata)
    #f.rows.data = i.rows
    print(f.rows.data)
    if bool(i):
        return render_template("invoice/edit.html", form=f, num=i.number)
    else:
        return redirect(url_for("invoices_index"))


@app.route("/invoices/<int:number>/edit/", methods=["GET"])
@login_required
def invoice_edit(number):
    i = Invoice.query.get(number)
    f = InvoiceForm()
    f.customer.data = i.customer
    f.rows.data = i.rows
    if bool(i):
        return render_template("invoice/edit.html", form=f, num=i.number)
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
    f = InvoiceForm()
    f.rows.append_entry()
    return render_template("invoice/edit.html", form=f, num=0)


@app.route("/invoices/", methods=["POST"])
@login_required
def invoice_create():
    f = InvoiceForm(request.form)
    rows = []
    for i in f.rows.data:
        if i["product"] and i["count"]:
            rows.append(Row(i["product"], i["count"]))
#    if not f.validate():
#        return render_template("invoice/edit.html", form=f, num=0)
    i = Invoice(f.customer.data, rows)
    if bool(i.customer.name):
        db.session().add(i)
        db.session().commit()
    return redirect(url_for("invoices_index"))


@app.route("/invoices/del/<int:number>/", methods=["GET"])
@login_required
def invoice_delete(number):
    i = Invoice.query.get(number)
    if bool(i):
        db.session().delete(i)
        db.session().commit()
    return redirect(url_for("invoices_index"))


@app.route("/invoices/<int:number>/rows/", methods=["POST"])
@login_required
def rows_add():
    f = InvoiceForm(request.form)
    #f.rows.append(Rows())
    return render_template("invoice/edit.html", form=f, num=number)

@app.route("/invoices/<int:number>/rows/<int:row>/", methods=["POST"])
@login_required
def rows_del():
    f = InvoiceForm(request.form)
    return render_template("invoice/edit.html", form=f, num=number)
