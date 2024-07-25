from flask import Blueprint, request, jsonify
from models.stocks_joiner import (
    get_bist_database_joiner,
    get_dow_jones_database_joiner,
    get_cryptocurrencies_database_joiner
    )

stocks_bp = Blueprint('stocks', __name__)

@stocks_bp.route('/bist-to-database/<string:sifre>', methods=['GET'])
def get_bist_to_database(sifre):
    if sifre == "bs498":
        bist = get_bist_database_joiner()
        return jsonify(bist)

@stocks_bp.route('/dow-jones-to-database/<string:sifre>', methods=['GET'])
def get_dow_jones_to_database(sifre):
    if sifre == "bs498":
        dow_jones = get_dow_jones_database_joiner()
        return jsonify(dow_jones)

@stocks_bp.route('/cryptocurrencies-to-database/<string:sifre>', methods=['GET'])
def get_cryptocurrencies_to_database(sifre):
    if sifre == "bs498":
        cryptocurrencies = get_cryptocurrencies_database_joiner()
        return jsonify(cryptocurrencies)
    
    
# @stocks_bp.route('/stocks/<string:locale>/<int:locale>', methods=['GET'])
# def get_stocks_by_locale_and_id(sifre):
#     cryptocurrencies = get_cryptocurrencies_database_joiner()
#     return jsonify(cryptocurrencies)