
from flask import render_template, url_for, flash, redirect
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog import app
from flaskblog.models import User, Post


posts = [
    {
        'author': 'Lucas Soares',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 21, 2018'
    },
    {
        'author': 'Maria Clara',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 23, 2018'
    }
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
        if form.email.data == 'lucaslebre138@gmail.com' and form.password.data == '123':
            flash(f'You have been logged in {form.email.data} !', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login Unsuccessful. Please check the Username or the Password', 'danger')
    return render_template('login.html', title='Register', form=form)