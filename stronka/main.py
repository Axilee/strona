from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '0862cdef2c287e81095d38a0380ff9ed'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///strona.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    avatar = db.Column(db.String(20), nullable=False, default='default.png')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.avatar}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"

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
    if form.username.data == 'Axile' and form.password.data == '123':
        flash('Zalogowano!', 'success')
        return redirect(url_for('home'))
    else:
        flash('Nie zalogowano.', 'danger')        
    return render_template('login.html', title='Login',form=form)
@app.route('/ok')
def problem():
    return render_template('problem.html', title='xddddd')

if __name__ == '__main__':
    app.run(debug=True)


