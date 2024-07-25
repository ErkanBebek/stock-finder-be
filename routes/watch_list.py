# routes/users.py
from flask import Blueprint, request, jsonify
from models.watch_list import (
    get_watch_list_by_userID,
    delete_watched_by_stocksID,
    add_watch_list
    )

watch_list_bp = Blueprint('watch_list', __name__)


# @app.route('/watch_list/slug/<string:slug>', methods=['GET'])
@watch_list_bp.route('/watch_list/<int:user_id>', methods=['GET'])
def get_watch_list(user_id):
    watch_list = get_watch_list_by_userID(user_id)
    return jsonify(watch_list)

@watch_list_bp.route('/watched_item', methods=['POST'])
def delete_watched():
    data = request.get_json()
    delete_watched_by_stocksID(data)
    return jsonify({'message': 'watched_item deleted successfully'}), 201


@watch_list_bp.route('/watch_list', methods=['POST'])
def create_watch_list_item():
    data = request.get_json()
    add_watch_list(data)
    return jsonify({'message': 'watched_item added successfully'}), 201