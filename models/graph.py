from flask import Flask, jsonify
import yfinance as yf
from datetime import datetime


# Alpha Vantage API anahtarınızı buraya ekleyin

def get_stock_data_for_candle(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1d", interval="1m")
    data = []
    for index, row in hist.iterrows():
        data.append({
            'close': row['Close'],
            'high': row['High'],
            'low': row['Low'],
            'open': row['Open'],
            'time': {
                'year': index.year,
                'month': index.month,
                'day': index.day,
                'hour': index.hour,
                'minute': index.minute
            }
        })
    
    # Verileri zaman damgasına göre sırala
    sorted_data = sorted(data, key=lambda x: (x['time']['year'], x['time']['month'], x['time']['day'], x['time']['hour'], x['time']['minute']))

    return sorted_data


def get_stock_data_for_area(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1d", interval="1m")  # Günlük verileri alıyoruz
    data = []

    for index, row in hist.iterrows():
        data.append({
            'time': index.strftime('%Y-%m-%d'),  # Zaman damgasını string formatına çeviriyoruz
            'value': row['Close']  # Kapanış fiyatını alıyoruz
        })
    
    return data