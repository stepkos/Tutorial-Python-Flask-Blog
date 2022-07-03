from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms import validators as val
from flaskblog.models import User


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

    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first():
            raise val.ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise val.ValidationError('That email is taken. Please choose a different one.')


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

 
class UpdateAccountForm(FlaskForm):

    username = StringField('Username', validators = [
        val.DataRequired(), 
        val.Length(min=2, max=20)
    ])

    email = StringField('Email', validators = [
        val.DataRequired(), 
        val.Email()
    ])

    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])

    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username and User.query.filter_by(username=username.data).first():
            raise val.ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email and User.query.filter_by(email=email.data).first():
            raise val.ValidationError('That email is taken. Please choose a different one.')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[val.DataRequired()])
    content = TextAreaField('Content', validators=[val.DataRequired()])
    submit = SubmitField('Post')
