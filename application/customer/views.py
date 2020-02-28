from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required
from application.customer.models import Customer
from application.customer.forms import CustomerForm
from application.invoice.models import Invoice

# Onko asiakkaalla laskuja?
def deletable(number):
    return Invoice.query.filter_by(customer_num=number).count() == 0

# Asiakasluettelo
@app.route("/customers/", methods=["GET"])
@login_required
def customers_index():
    last = int((Customer.query.count()-1)/5)+1
    last = last if last > 0 else 1
    page = request.args.get('page', default=1, type=int)
    page = page if page >= 1 else 1
    page = page if page <= last else last
    customers = Customer.query.paginate(
        page=page, per_page=5, error_out=False).items
    return render_template("customer/list.html", customers=customers, page=page, last=last)

# Asiakkaan muokkauslomake
@app.route("/customers/<int:number>/", methods=["GET"])
@login_required
def customer_edit(number):
    cust = Customer.query.get(number)
    form = CustomerForm()
    form.name.data = cust.name
    form.address.data = cust.address
    if bool(cust):
        return render_template("customer/edit.html", form=form, num=cust.number, delete=deletable(cust.number))
    else:
        return redirect(url_for("customers_index"))

# Muokatun asiakkaan tallennus
@app.route("/customers/<int:number>/", methods=["POST"])
@login_required
def customer_save(number):
    form = CustomerForm(request.form)
    if not form.validate():
        return render_template("customer/edit.html", form=form, num=number, delete=deletable(number))
    cust = Customer.query.get(number)
    if bool(cust) and bool(form.name.data):
        cust.name = form.name.data
        cust.address = form.address.data
        db.session().commit()
    return redirect(url_for("customers_index"))

# Uuden asiakkaan luomislomake
@app.route("/customers/new/", methods=["GET"])
@login_required
def customer_form():
    return render_template("customer/edit.html", form=CustomerForm(), num=0, delete=False)

# Uuden asiakkaan tallennus
@app.route("/customers/", methods=["POST"])
@login_required
def customer_create():
    form = CustomerForm(request.form)
    if not form.validate():
        return render_template("customer/edit.html", form=form, num=0, delete=False)
    cust = Customer(form.name.data, form.address.data)
    if bool(cust.name):
        db.session().add(cust)
        db.session().commit()
    return redirect(url_for("customers_index"))

# Asiakkaan poistaminen
@app.route("/customers/del/<int:number>/", methods=["GET"])
@login_required
def customer_delete(number):
    cust = Customer.query.get(number)
    if bool(cust) and deletable(number):
        db.session().delete(cust)
        db.session().commit()
    return redirect(url_for("customers_index"))
