from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.invoice.models import Invoice
from application.invoice.forms import InvoiceForm
from application.row.models import Row
from application.customer.models import Customer
from application.product.models import Product


@app.route("/init/", methods=["GET"])
@login_required
def invoices_init():
    cust = Customer.query.first()
    prod = Product.query.first()
    row = Row(prod, 1)
    inv = Invoice(cust, [row])
    db.session().add(row)
    db.session().add(inv)
    db.session().commit()
    return render_template("invoice/list.html", invoices=Invoice.query.all())


def check_access(num):
    for inv in current_user.invoices:
        if inv.number == num:
            return True
    return False



@app.route("/invoices/", methods=["GET"])
@login_required
def invoices_index():
    last = int((len(current_user.invoices)-1)/5)+1
    last = last if last > 0 else 1
    page = request.args.get('page', default = 1, type = int)
    page = page if page >= 1 else 1
    page = page if page <= last else last
    invoices = Invoice.query.filter_by(account_id=current_user.id).paginate(page=page, per_page=5, error_out=False).items
    return render_template("invoice/list.html", invoices=invoices, page=page, last=last)


@app.route("/invoices/edit/<int:number>/", methods=["GET"])
@login_required
def invoice_edit(number):
    if not check_access(number):
        return redirect(url_for("invoices_index"))
    inv = Invoice.query.get(number)
    form = InvoiceForm()
    form.customer.data = inv.customer
    for row in inv.rows:
        form.rows.append_entry({"product": row.product, "qty": row.qty})
    form.rows.append_entry()
    form.rows.append_entry()
    if bool(inv):
        return render_template("invoice/edit.html", form=form, num=inv.number)
    else:
        return redirect(url_for("invoices_index"))


@app.route("/invoices/<int:number>/", methods=["GET"])
@login_required
def invoice_show(number):
    if not check_access(number):
        return redirect(url_for("invoices_index"))
    inv = Invoice.query.get(number)
    total = 0
    for row in inv.rows:
        total += row.product.price*row.qty
    if bool(inv):
        return render_template("invoice/show.html", inv=inv, tot=total)
    else:
        return redirect(url_for("invoices_index"))


@app.route("/invoices/<int:number>/", methods=["POST"])
@login_required
def invoice_save(number):
    if not check_access(number):
        return redirect(url_for("invoices_index"))
    form = InvoiceForm(request.form)
    if not form.validate():
        return render_template("invoice/edit.html", form=form, num=number)
    rows = []
    for formRow in form.rows.data:
        try:
            qty = float(formRow["qty"])
        except ValueError:
            continue
        if formRow["product"] and qty > 0:
            rows.append(Row(formRow["product"], qty))
    inv = Invoice(form.customer.data, rows)
    inv.number = number
    if bool(inv) and bool(inv.customer) and bool(inv.customer.name) and len(inv.rows) > 0:
        old = Invoice.query.get(number)
        if bool(old):
            db.session().delete(old)
        db.session().add(inv)
        for row in inv.rows:
            db.session().add(row)
        db.session().commit()
    return redirect(url_for("invoices_index"))


@app.route("/invoices/new/", methods=["GET"])
@login_required
def invoice_form():
    form = InvoiceForm()
    for i in range(5):
        form.rows.append_entry()
    return render_template("invoice/edit.html", form=form, num=0)


@app.route("/invoices/", methods=["POST"])
@login_required
def invoice_create():
    form = InvoiceForm(request.form)
    if not form.validate():
        return render_template("invoice/edit.html", form=form, num=0)
    rows = []
    for formRow in form.rows.data:
        try:
            qty = float(formRow["qty"])
        except ValueError:
            continue
        if formRow["product"] and qty >= 0:
            rows.append(Row(formRow["product"], qty))
    inv = Invoice(form.customer.data, rows)
    if bool(inv) and bool(inv.customer) and bool(inv.customer.name) and len(inv.rows) > 0:
        db.session().add(inv)
        for row in inv.rows:
            db.session().add(row)
        db.session().commit()
    return redirect(url_for("invoices_index"))


@app.route("/invoices/del/<int:number>/", methods=["GET"])
@login_required
def invoice_delete(number):
    if not check_access(number):
        return redirect(url_for("invoices_index"))
    inv = Invoice.query.get(number)
    if bool(inv):
        db.session().delete(inv)
        db.session().commit()
    return redirect(url_for("invoices_index"))
