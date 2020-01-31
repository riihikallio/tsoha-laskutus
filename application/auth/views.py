from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm(), action="auth_login", button="Login")

    form = LoginForm(request.form)
    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")

    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/new", methods=["GET"])
def auth_new():
    return render_template("auth/loginform.html", form=LoginForm(), action="auth_create", button="Create")

@app.route("/auth/new", methods=["POST"])
def auth_create():
    f = LoginForm(request.form)
    if not f.validate():
        return render_template("auth/loginform.html", form=f, action="auth_create", button="Create")
    u = User(f.username.data, f.username.data, f.password.data)
    if bool(u.name):
        db.session().add(u)
        db.session().commit()
        login_user(u)
    return redirect(url_for("products_index"))