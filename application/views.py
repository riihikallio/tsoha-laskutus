from flask import render_template
from application import app

@app.route("/")
def index():
    return redirect(url_for("customers_index"))