from flaskProjectTest import db, api

from flask import jsonify, request
from flask_pydantic import validate
from flask_restx import Resource
from flaskProjectTest.model import Book
from flaskProjectTest.api_model import book_model, book_post_model
from flaskProjectTest.pydantic_model import RequestBodyModel


@api.route('/book')
class Books(Resource):

    @api.marshal_list_with(book_model, code=200, envelope="books")
    def get(self):
        books = Book.query.all()
        return books

    # @api.marshal_with(book_model, code=201)
    @api.expect(book_post_model)
    @validate()
    def post(self, body: RequestBodyModel):
        title = body.title
        author = body.author
        new_book = Book(title=title, author=author)

        db.session.add(new_book)
        db.session.commit()

        return jsonify({'msg': 'New book has been created'})


@api.route('/book/<int:id>')
class BookResource(Resource):

    @api.marshal_with(book_model, code=200, envelope="book")
    def get(self, id):
        book = Book.query.get_or_404(id)
        return book

    @api.marshal_with(book_model, code=200, envelope="book")
    @api.expect(book_model)
    def put(self, id):
        book_to_update = Book.query.get_or_404(id)

        data = request.get_json()

        book_to_update.title = data.get('title')
        book_to_update.author = data.get('author')
        db.session.commit()

        return book_to_update

    @api.marshal_with(book_model, envelope="book_deleted", code=200)
    def delete(self, id):
        book_to_delete = Book.query.get_or_404(id)
        db.session.delete(book_to_delete)
        db.session.commit()
        return book_to_delete
