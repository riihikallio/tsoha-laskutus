from application import app, db
from flask import redirect, render_template, request, url_for
from application.customer.models import Customer


@app.route("/invoices/", methods=["GET"])
def invoices_index():
    return render_template("invoice/list.html")
