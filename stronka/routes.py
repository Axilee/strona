from stronka.models import User, Post
from flask import render_template, url_for, flash, redirect
from stronka.forms import RegistrationForm, LoginForm
from stronka import app
posts = [ 
    { 
        "autor": 'Kacper Fitas',
        'tytul': 'Post pierwszy',
        'content': 'hejo pierwszy post',
        'data': '11.04.2020'
    },
    {
        "autor": 'Kacper Drugi Fitas',
        'tytul': 'Post drugi',
        'content': 'hejo drugi post',
        'data': '12.04.2020'
    }
]


@app.route("/")
@app.route("/home")
def home(): 
    return render_template("home.html", posts=posts)


@app.route("/about")
def about(): 
    return render_template('about.html', title="About")

@app.route('/register', methods=['GET', 'POST'])
def register(): 
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Stworzono konto dla {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register',form=form)

@app.route('/login', methods=['GET', 'POST'])
def login(): 
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'Axile' and form.password.data == '123':
            flash('Zalogowano!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Nie zalogowano.', 'danger')        
    return render_template('login.html', title='Login',form=form)
@app.route('/ok')
def problem():
    return render_template('problem.html', title='xddddd')
