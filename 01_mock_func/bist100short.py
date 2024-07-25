import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify

# Flask uygulamasını başlatıyoruz.
app = Flask(__name__)

# '/fetch-stock-data' URL'ine gelen GET isteklerini işleyecek bir rota tanımlıyoruz.
@app.route('/fetch-stock-data', methods=['GET'])
def fetch_stock_data():
    url = 'https://bigpara.hurriyet.com.tr/borsa/canli-borsa/'

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
        # '.live-stock-item' sınıfına sahip tüm HTML elemanlarını seçiyoruz.
        for item in soup.select('.live-stock-item'):
            # Her bir hisse senedi elemanından gerekli verileri çekiyoruz.
            name = item.select_one('a').decode
            last = item.select_one('.node-c').text
            bid = item.select_one('.node-f').text
            ask = item.select_one('.node-g').text
            high = item.select_one('.node-h').text
            low = item.select_one('.node-i').text
            weighted_average = item.select_one('.node-j').text
            change = item.select_one('.node-e').text
            status = item.select_one('.node-direction')['class'][2]

            # Çekilen verileri bir sözlük halinde listeye ekliyoruz.
            stock_data.append({
                'name': name,
                'last': last,
                'bid': bid,
                'ask': ask,
                'high': high,
                'low': low,
                'weighted_average': weighted_average,
                'change': change,
                'status': status
            })

        # JSON formatında hisse senedi verilerini döndürüyoruz.
        return jsonify(stock_data), 200
    except Exception as e:
        # Hata durumunda JSON formatında hata mesajı döndürüyoruz.
        return jsonify({'error': f'Veriler çekilirken hata oluştu: {str(e)}'}), 500

# Flask uygulamasını çalıştırıyoruz.
if __name__ == '__main__':
    app.run(debug=True)
