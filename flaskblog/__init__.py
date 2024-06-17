from flask import Flask
# from flaskblog.forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SECRET_KEY'] = '0a862f8f59064e19edb46fc3a7729154'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.app_context().push()    


from flaskblog import routes