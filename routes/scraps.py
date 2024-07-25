from flask import Blueprint, request, jsonify
from models.scraps import (
    get_bist_data,
    get_economic_calendar_data,
    get_global_index_data,
    #get_nasdaq_100_data,
    get_dow_jones_30_data,
    get_cryptocurrencies_data,
    get_bist_XU100_data
)

scraps_bp = Blueprint('scraps', __name__)

@scraps_bp.route('/bist', methods=['GET'])
def get_bist():
    bist = get_bist_data()
    return jsonify(bist)

@scraps_bp.route('/bist_tw', methods=['GET'])
def get_bist_xu100():
    bist = get_bist_XU100_data()
    return jsonify(bist)

@scraps_bp.route('/economic-calendar', methods=['GET'])
def get_economic_calendar():
    economic_calendar = get_economic_calendar_data()
    return jsonify(economic_calendar)

@scraps_bp.route('/global-index', methods=['GET'])
def get_global_index():
    global_index = get_global_index_data()
    return jsonify(global_index)


# @scraps_bp.route('/nasdaq_100', methods=['GET'])
# def get_nasdaq_100():
#     nasdaq_100 = get_nasdaq_100_data()
#     return jsonify(nasdaq_100)

@scraps_bp.route('/dow_jones', methods=['GET'])
def get_dowjones30():
    dowjones = get_dow_jones_30_data()
    return jsonify(dowjones)


@scraps_bp.route('/cryptocurrencies', methods=['GET'])
def get_cryptocurrencies():
    cryptocurrencies = get_cryptocurrencies_data()
    return jsonify(cryptocurrencies)