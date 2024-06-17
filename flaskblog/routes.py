from flaskblog import app, db, bcrypt
from flask import Flask, render_template, url_for
from flask import flash, redirect
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post


posts = [
    {
        'author': 'Yosef Alemu',
        'title': 'My blog post',
        'content': 'first content',
        'date_posted': 'april 20, 2028'
    },
    {
        'author': 'yared',
        'title': 'The Trade',
        'content': 'merkato',
        'date_content': ' april 2,45'

    }
]


@app.route('/', strict_slashes=False)
@app.route('/home', strict_slashes=False)
def home():
    """ Prints a Message when / is called """
    return render_template('home.html', posts=posts)


@app.route('/about', strict_slashes=False)
def about():
    """ Prints a Message when /about is called """
    return render_template('about.html', posts=posts, title='About!!')


@app.route('/register', methods=['GET', 'POST'], strict_slashes=False)
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data,
                    password=hashed_password)   
        db.session.add(user)
        db.session.commit()
        flash('Your account has been crated you are now ale to login', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Log-in', form=form)