from application import app, db
from flask import redirect, render_template, request, url_for
from application.customer.models import Customer


@app.route("/products/", methods=["GET"])
def products_index():
    return render_template("product/list.html")
