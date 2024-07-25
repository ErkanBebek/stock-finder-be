# routes/users.py
from flask import Blueprint, request, jsonify
from models.graph import (
    get_stock_data_for_candle,
    get_stock_data_for_area
    )

graph_bp = Blueprint('graph', __name__)


@graph_bp.route('/candle/<string:locale>/<string:stock_symbol>/', methods=['GET'])
def get_candle_data(stock_symbol,locale):
    if locale == "TR":
        data  = get_stock_data_for_candle(stock_symbol+".IS")
    elif locale == "US":
        data  = get_stock_data_for_candle(stock_symbol)
    elif locale == "World":
        data  = get_stock_data_for_candle(stock_symbol+"-USD")
    return jsonify(data)


@graph_bp.route('/area/<string:locale>/<string:stock_symbol>/', methods=['GET'])
def get_area_data(stock_symbol,locale):
    if locale == "TR":
        data  = get_stock_data_for_area(stock_symbol+".IS")
    elif locale == "US":
        data  = get_stock_data_for_area(stock_symbol)
    elif locale == "World":
        data  = get_stock_data_for_area(stock_symbol+"-USD")
    return jsonify(data)
