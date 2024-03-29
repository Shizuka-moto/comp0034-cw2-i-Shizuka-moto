from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Note, Expenditure, Enrolment, institutional_distribution
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

# Define the authentication blueprint
auth = Blueprint('auth', __name__)

# Login route
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

# Logout route
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

# Education expenditure route
@auth.route('/Education_expenditure', methods=['GET', 'POST'])
@login_required
def Education_expenditure():
    Time = None
    if request.method == 'POST':
        Years = request.form.get('Years')
        Time = Expenditure.query.filter_by(Years=Years).first()
        if Time:
            flash('Data found!', category='success')
        else:
            flash('Data not found', category='error')
    return render_template("expenditure.html", Expenditure=Time, user=current_user)

# Education enrolment route
@auth.route('/Education_enrolment', methods=['GET', 'POST'])
@login_required
def Education_enrolment():
    Time = None
    if request.method == 'POST':
        Years = request.form.get('Years')
        Time = Enrolment.query.filter_by(Years=Years).first()
        if Time:
            flash('Data found!', category='success')
        else:
            flash('Data not found', category='error')
    return render_template("enrolment.html", Enrolment=Time, user=current_user)

# Institute distribution route
@auth.route('/Institute_distribution', methods=['GET', 'POST'])
@login_required
def Institute_distribution():
    Time = None
    if request.method == 'POST':
        Years = request.form.get('Years')
        Time = institutional_distribution.query.filter_by(Years=Years).first()
        if Time:
            flash('Data found!', category='success')
        else:
            flash('Data not found', category='error')
    return render_template("institutional_distribution.html", institutional_distribution=Time, user=current_user)
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    # Check if the request method is POST
    if request.method == 'POST':
        # Get form data
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # Check if the email already exists
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        # Validate form data
        elif len(email) < 1:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 1:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords does not match.', category='error')
        elif len(password1) < 5:
            flash('Password must be more than 5 characters.', category='error')
        else:
            # Create a new user and add to the database
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()

            # Log in the user and redirect to home
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    # Render the sign-up template
    return render_template("sign_up.html", user=current_user)
