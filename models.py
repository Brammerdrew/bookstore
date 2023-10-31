from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_marshmallow import Marshmallow
import secrets

db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key=True)
    first_name = db.Column(db.String(length=150), nullable=True, default='')
    last_name = db.Column(db.String(length=150), nullable=True, default='')
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False, default='')
    token = db.Column(db.String, default='', unique=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    

    def __init__(self, first_name='', last_name='', email='', password='', token='', id=''):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = self.set_password(password)
        self.token = self.set_token(24)
    
    def set_token(self, length):
        return secrets.token_hex(length)

    def set_id(self):
        return str(uuid.uuid4())
    
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash
    
    def __repr__(self):
        return f'User {self.email} has been created and added to the database!'
    

class Books(db.Model):
    id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String(length=150), nullable=False, default='')
    author = db.Column(db.String(length=150), nullable=False, default='')
    genre = db.Column(db.String(length=150), nullable=False, default='')
    isbn = db.Column(db.String(length=150), nullable=False, default='')
    hardcover = db.Column(db.Boolean, nullable=False, default=False)
    length = db.Column(db.Integer, nullable=False, default=0)
    price = db.Column(db.Integer, nullable=False, default=0)
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable=False)
    
    def __init__(self, title='', author='', genre='', isbn='', hardcover=False, length=0, price=0, user_token='', id=''):
        self.id = self.set_id()
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        self.hardcover = hardcover
        self.length = length
        self.price = price
        self.user_token = user_token

    def __repr__(self):
        return f'The following book has been added: {self.title} by {self.author}'
    
    def set_id(self):
        return (secrets.token_urlsafe())
    
class BooksSchema(ma.Schema):
    class Meta:
        fields = ['id', 'title', 'author', 'genre', 'isbn', 'hardcover', 'length', 'price']

book_schema = BooksSchema()
books_schema = BooksSchema(many=True)
