import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify
import time  # Bekleme süresi eklemek için kullanılır

# Flask uygulamasını başlatıyoruz.
app = Flask(__name__)

# '/fetch-indices-data' URL'ine gelen GET isteklerini işleyecek bir rota tanımlıyoruz.
@app.route('/fetch-indices-data', methods=['GET'])
def fetch_indices_data():
    url = 'https://finance.yahoo.com/world-indices/'

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
        # Bekleme süresi ekliyoruz (5 saniye)
        time.sleep(5)

        # Tablodaki tüm satırları dolaşıyoruz.
        for element in soup.select('tr'):
            # Sembol, isim, son fiyat, değişim, yüzde değişim ve hacim bilgilerini çekiyoruz.
            symbol_elem = element.select_one('[aria-label="Symbol"]')
            name_elem = element.select_one('[aria-label="Name"]')
            last_elem = element.select_one('[aria-label="Last Price"]')
            change_elem = element.select_one('[aria-label="Change"]')
            percentage_change_elem = element.select_one('[aria-label="% Change"]')
            volume_elem = element.select_one('[aria-label="Volume"]')

            symbol = symbol_elem.text.strip() if symbol_elem else 'N/A'
            name = name_elem.text.strip() if name_elem else 'N/A'
            last = last_elem.text.strip() if last_elem else 'N/A'
            change = change_elem.text.strip() if change_elem else 'N/A'
            percentage_change = percentage_change_elem.text.strip() if percentage_change_elem else 'N/A'
            volume = volume_elem.text.strip() if volume_elem else 'N/A'

            # Sembol bilgisi boş değilse veriyi listeye ekliyoruz.
            if symbol and symbol != 'N/A':
                stock_data.append({
                    'symbol': symbol,
                    'name': name,
                    'last': last,
                    'change': change,
                    'percentage_change': percentage_change,
                    'volume': volume
                })

        # JSON formatında hisse senedi verilerini döndürüyoruz.
        return jsonify({'stockData': stock_data}), 200
    except Exception as e:
        # Hata durumunda JSON formatında hata mesajı döndürüyoruz.
        return jsonify({'error': f'Veriler çekilirken hata oluştu: {str(e)}'}), 500

# Flask uygulamasını çalıştırıyoruz.
if __name__ == '__main__':
    app.run(debug=True)
