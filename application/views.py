from flask import redirect
from application import app

@app.route("/")
def index():
    return redirect(url_for("customers_index"))