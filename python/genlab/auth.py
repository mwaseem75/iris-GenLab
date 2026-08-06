from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from .models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__)

# Login


@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                return redirect(url_for('views.index'))
            else:
                flash('Password is incorrect.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


# Register user
@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get("email")
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        email_exists = User.query.filter_by(email=email).first()
        username_exists = User.query.filter_by(username=username).first()

        if email_exists:
            flash('Email is already in use.', category='error')
        elif username_exists:
            flash('Username is already in use.', category='error')
        elif password1 != password2:
            flash('Password don\'t match!', category='error')
        elif len(username) < 2:
            flash('Username is too short.', category='error')
        elif len(password1) < 6:
            flash('Password is too short.', category='error')
        elif len(email) < 4:
            flash("Email is invalid.", category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(
                password1))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            return redirect(url_for('views.index'))

    return render_template("signup.html", user=current_user)

# Change password


@auth.route("/change-password", methods=['GET', 'POST'])
@login_required
def change_password():
    if request.method == 'POST':
        email = request.form.get("email")
        old_password = request.form.get("old_password")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, old_password):
                if password1 != password2:
                    flash('Password don\'t match!', category='error')
                elif old_password == password1:
                    flash('Old and New Password is same', category='error')
                elif len(password1) < 6:
                    flash('Password is too short', category='error')
                else:
                    user.password = generate_password_hash(password1)
                    db.session.commit()
                    login_user(user, remember=True)
                    flash('Password changed successfully', category='error')
                    return redirect(url_for('views.index'))
            else:
                flash('Old Password is not correct', category='error')
        else:
            flash('Email Id not found.', category='error')

    return render_template("change_password.html", user=current_user)

# Sign out


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.index"))