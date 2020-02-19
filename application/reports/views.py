from flask import render_template
from flask_login import login_required

from application import app
from application.reports.models import sales_by_category, sales_by_customer

@app.route("/reports/", methods=["GET"])
@login_required
def reports():
    return render_template("reports/show.html", cat=sales_by_category(), cust=sales_by_customer())
