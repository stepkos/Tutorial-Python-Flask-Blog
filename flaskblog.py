from flask import Flask, render_template, url_for, flash, redirect
from forms import *

app = Flask(__name__)
app.config['SECRET_KEY'] = '39022dcb1591401466fdfe2809f1fc2b'


posts = [
    {
        'author': 'Jakub Stepkowski',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'June 30, 2022'
    },
    {
        'author': 'Jan Kowalski',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'July 1, 2022'
    },
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Register', form=form)



if __name__ == '__main__':
    app.run(debug=True)