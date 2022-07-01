from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms import validators as val


class RegistrationForm(FlaskForm):

    username = StringField('Username', validators = [
        val.DataRequired(), 
        val.Length(min=2, max=20)
    ])

    email = StringField('Email', validators = [
        val.DataRequired(), 
        val.Email()
    ])

    password = PasswordField('Password', validators = [
        val.DataRequired()
    ])

    confirm_password = PasswordField('Confirm password', validators = [
        val.DataRequired(),
        val.EqualTo('password')
    ])

    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):

    email = StringField('Email', validators = [
        val.DataRequired(), 
        val.Email()
    ])

    password = PasswordField('Password', validators = [
        val.DataRequired()
    ])

    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')