#!/usr/bin/python3
""" Starts a Flash Web Application """
from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy 
from flask import flash, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = '0a862f8f59064e19edb46fc3a7729154' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

posts = [
    {
        'author': 'Yosef Alemu',
        'title': 'My blog post',
        'content': 'first content',
        'date_posted': 'april 20, 2028'
    },
    {
        'author':'yared',
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
    return render_template('about.html', posts=posts, title = 'About!!')


@app.route('/register', methods=['GET','POST'], strict_slashes=False)
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET','POST'], strict_slashes=False)
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Log-in', form=form)

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug=True)
