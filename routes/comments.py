# routes/users.py
from flask import Blueprint, request, jsonify
from models.comments import (
    get_comments_by_stock_symbol,
    add_comment
    )

comments_bp = Blueprint('comments', __name__)


# @app.route('/comments/slug/<string:slug>', methods=['GET'])
@comments_bp.route('/comments/<string:locale>/<string:stock_symbol>', methods=['GET'])
def get_comment(stock_symbol,locale):
    comment = get_comments_by_stock_symbol(stock_symbol,locale)
    return jsonify(comment)

@comments_bp.route('/comment', methods=['POST'])
def create_user():
    data = request.get_json()
    add_comment(data)
    return jsonify({'message': 'comment added successfully'}), 201