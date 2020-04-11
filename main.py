from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '0862cdef2c287e81095d38a0380ff9ed'

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

@app.route('/login')
def login(): 
    form = LoginForm()
    return render_template('login.html', title='Login',form=form)
@app.route('/ok')
def problem():
    return render_template('problem.html', title='xddddd')

if __name__ == '__main__':
    app.run(debug=True)


