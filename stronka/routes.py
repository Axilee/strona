from stronka.models import User, Post
from flask import render_template, url_for, flash, redirect, request
from stronka.forms import RegistrationForm, LoginForm
from stronka import app,db,bcrypt
from flask_login import login_user, current_user, logout_user, login_required
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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed)
        db.session.add(user)
        db.session.commit()
        flash(f'Stworzono konto!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register',form=form)

@app.route('/login', methods=['GET', 'POST'])
def login(): 
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user,remember = form.remember.data)
            flash(f'Witaj, panie {form.username.data }', 'success')
            next_page = request.args.get('next')
            return redirect (next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Coś nie tak.', 'danger')        
    return render_template('login.html', title='Login',form=form)
@app.route('/ok')
def problem():
    return render_template('problem.html', title='xddddd')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account')
@login_required
def account():
    return render_template('account.html')