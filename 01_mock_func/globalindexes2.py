import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify

# Flask uygulamasını başlatıyoruz.
app = Flask(__name__)

# '/fetch-indices-data' URL'ine gelen GET isteklerini işleyecek bir rota tanımlıyoruz.
@app.route('/fetch-indices-data2', methods=['GET'])
def fetch_indices_data():
    url = 'https://markets.businessinsider.com/indices'

    try:
        # Belirtilen URL'ye HTTP GET isteği gönderiyoruz.
        response = requests.get(url)
        # İsteğin başarılı olup olmadığını kontrol ediyoruz.
        response.raise_for_status()
        # Gelen HTML içeriğini alıyoruz.
        html = response.content
        # BeautifulSoup ile HTML içeriğini ayrıştırıyoruz.
        soup = BeautifulSoup(html, 'html.parser')

        stock_data = []
# Tablodaki her bir satırı dolaşma
        for row in soup.select('tbody > tr'):
            # Sembolü çekme
            symbol = row.select_one('a.deep-sea-blue')['title']
            print(symbol)
            # Ülke bilgisini çekme
            symbolcountry = row.select_one('td').decode_contents().split("<br>")[1].strip()
            print(symbolcountry)
            
            # Son fiyatı çekme
            last = row.select('td.text-right')[0].decode_contents().split("<br>")[0].strip()
            # Önceki kapanış fiyatını çekme
            prev_close = row.select('td.text-right')[0].decode_contents().split("<br>")[1].strip()
            # Denge bilgisini çekme
            balance = row.select('td.text-right')[0].find('span').text
            # Yüzde değişim bilgisini çekme
            percentage_change = row.select('td.text-right')[1].text.strip().split("\n")[1]
            # Zaman bilgisini çekme
            time = row.select('td.text-right')[2].find('span').text
            # Tarih bilgisini çekme
            date = row.select('td.text-right')[2].text.strip().split("\n")[1]
            # Yıl başından bugüne değişim bilgisini çekme
            ytd = row.select('td.text-right')[-1].text.strip().split("\n")[0]
            # Bir yıllık değişim bilgisini çekme
            one_year = row.select('td.text-right')[-1].text.strip().split("\n")[1]

            # Sembol null değilse veriyi listeye ekle
            if symbol:
                stock_data.append({
                    'symbol': symbol,
                    'symbolcountry': symbolcountry,
                    'last': last,
                    'prev_close': prev_close,
                    'balance': balance,
                    'percentage_change': percentage_change,
                    'time': time,
                    'date': date,
                    'ytd': ytd,
                    'one_year': one_year
                })

        # JSON formatında hisse senedi verilerini döndürüyoruz.
        return jsonify({'stockData': stock_data}), 200
    except Exception as e:
        # Hata durumunda JSON formatında hata mesajı döndürüyoruz.
        return jsonify({'error': f'Veriler çekilirken hata oluştu: {str(e)}'}), 500

# Flask uygulamasını çalıştırıyoruz.
if __name__ == '__main__':
    app.run(debug=True)
