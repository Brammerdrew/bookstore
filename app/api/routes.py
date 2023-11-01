from flask import Blueprint, jsonify, request, render_template
from helpers import token_required
from models import db, User, Books, book_schema, books_schema

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/getdata')
def getdata():
    return {'some': 'value'}

@api.route('/books', methods=['POST'])
@token_required
def create_book(current_user_token):
    title = request.json['title']
    author = request.json['author']
    genre = request.json['genre']
    isbn = request.json['isbn']
    hardcover = request.json['hardcover']
    length = request.json['length']
    price = request.json['price']
    user_token = current_user_token.token

    print(f'TESTER: {current_user_token.token}')

    book = Books(title, author, genre, isbn, hardcover, length, price, user_token=user_token)

    db.session.add(book)
    db.session.commit()

    response = book_schema.dump(book)
    return jsonify(response)

@api.route('/books', methods=['GET'])
@token_required
def get_books(current_user_token):
    owner = current_user_token.token
    books = Books.query.filter_by(user_token=owner).all()
    response = books_schema.dump(books)
    return jsonify(response)

@api.route('/books/<id>', methods=['GET'])
@token_required
def get_book(current_user_token, id):
    token = current_user_token.token
    book = Books.query.get(id)
    response = book_schema.dump(book)
    return jsonify(response)

    
@api.route('/books/<id>', methods=['POST', 'PUT'])
@token_required
def update_book(current_user_token, id):
    book = Books.query.get(id)
    book.title = request.json['title']
    book.author = request.json['author']
    book.genre = request.json['genre']
    book.isbn = request.json['isbn']
    book.hardcover = request.json['hardcover']
    book.length = request.json['length']
    book.price = request.json['price']
    book.user_token = current_user_token.token

    db.session.commit()
    response = book_schema.dump(book)
    return jsonify(response)

@api.route('/books/<id>', methods=['DELETE'])
@token_required
def delete_book(current_user_token, id):
    book = Books.query.get(id)
    db.session.delete(book)
    db.session.commit()

    response = book_schema.dump(book)
    return jsonify(response)