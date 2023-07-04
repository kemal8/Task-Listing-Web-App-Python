from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_passwoed_hash
from . import db   ##means from __init__.py import db

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    # data = request.form
    # print(data)
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            # pass
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            # pass
            flash('First name must be greater than 1 characters.', category='error')
        elif password1 != password2:
            # pass
            flash('Password don\'t match', category='error')
        elif len(password1) < 7:
            # pass
            flash('Password must be at least 7 characters.', category='error')
        else:
            #USER CREATE IN DB
            # pass
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account Created!', category='success')
            return redirect(url_for('view.home'))


    return render_template("sign_up.html")

