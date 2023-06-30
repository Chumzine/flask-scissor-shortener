from flask_login import logout_user, current_user, login_required, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from ..extensions import db, login_manager, limiter
from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models.users import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError


auth = Blueprint('auth', __name__)
login_manager.login_view = "auth.login"


class RegisterForm(FlaskForm):
    first_name = StringField('First_name', validators=[
                            InputRequired(), Length(min=3, max=20)], render_kw={"placeholder": "First Name"})
    last_name = StringField('Last_name', validators=[
                            InputRequired(), Length(min=3, max=30)], render_kw={"placeholder": "Last name"})
    username = StringField('Username', validators=[
                           InputRequired(), Length(min=3, max=15)], render_kw={"placeholder": "Username"})
    email = StringField('Email', validators=[
                        InputRequired(), Length(min=10, max=50)], render_kw={"placeholder": "Email"})
    password = PasswordField('Password', validators=[
                             InputRequired(), Length(min=8, max=30)], render_kw={"placeholder": "Password"})
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                'Username already exists. Please choose a different one.')

    def validate_email(self, email):
        email_exists = User.query.filter_by(email=email.data).first()
        if email_exists:
            raise ValidationError(
                'Email already exists. Please choose a different one.')



class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
                           InputRequired(), Length(min=3, max=15)], render_kw={"placeholder": "Username"})
    password = PasswordField('Password', validators=[
                             InputRequired(), Length(min=8, max=30)],render_kw={"placeholder": "Password"} )
    submit = SubmitField('Login')



@auth.route('/register', methods=['GET', 'POST'])
@limiter.limit("100/hour")
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        password_hash = generate_password_hash(form.password.data, method='sha256')

        new_user = User(first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    username=form.username.data,
                    email=form.email.data,
                    password_hash=password_hash
                    )
        db.session.add(new_user)
        db.session.commit()
        flash('You were successfully registered')
        return redirect(url_for('auth.login'))

    return render_template('register.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
@limiter.limit("100/hour")
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(
                username=form.username.data).first()

            if user:
                if check_password_hash(user.password_hash, form.password.data):
                    login_user(user)
                    flash('You were successfully logged in')
                    return redirect(url_for('shorts.index'))
                else:
                    flash('Invalid username or password')
                    return redirect(url_for('auth.login'))
            else:
                flash('Invalid username or password')
                return redirect(url_for('auth.login'))
    return render_template('login.html', form=form)


@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('You were successfully logged out')
    return redirect(url_for('shorts.index'))