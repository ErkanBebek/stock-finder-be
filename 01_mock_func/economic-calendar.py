import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify

# Flask uygulamasını başlatıyoruz.
app = Flask(__name__)

# '/fetch-calendar-data' URL'ine gelen GET isteklerini işleyecek bir rota tanımlıyoruz.
@app.route('/fetch-calendar-data', methods=['GET'])
def fetch_calendar_data():
    url = 'https://fred.stlouisfed.org/releases/calendar'

    try:
        # Belirtilen URL'ye HTTP GET isteği gönderiyoruz.
        response = requests.get(url)
        # İsteğin başarılı olup olmadığını kontrol ediyoruz.
        response.raise_for_status()
        # Gelen HTML içeriğini alıyoruz.
        html = response.content
        # BeautifulSoup ile HTML içeriğini ayrıştırıyoruz.
        soup = BeautifulSoup(html, 'html.parser')

        # Tüm tarihleri ve olayları içeren bir sözlük oluşturuyoruz.
        data = {}

        # Tablodaki tüm satırları dolaşıyoruz.
        for element in soup.select('table.table-condensed tbody tr'):
            # Tarih bilgilerini çekiyoruz.
            date_elem = element.select_one('span[style="font-weight: bold;"]')
            date = date_elem.text.strip() if date_elem else None
            if date:
                # Eğer bu tarih daha önce eklenmediyse sözlüğe ekliyoruz.
                if date not in data:
                    data[date] = []
            else:
                # Saat ve olay adını çekiyoruz.
                time_elem = element.select_one('td[style="width:5%; text-align:right"]')
                event_elem = element.select_one('td[text-align="left"] a')

                time = time_elem.text.strip() if time_elem else 'NaN'
                event = event_elem.text.strip() if event_elem else None

                # Sadece saat ve olay adı dolu olan satırları işliyoruz.
                if time and event and data:
                    last_date = list(data.keys())[-1]
                    data[last_date].append({'time': time, 'event': event})

        # JSON formatında tarih ve olay verilerini döndürüyoruz.
        return jsonify({'dates': data}), 200
    except Exception as e:
        # Hata durumunda JSON formatında hata mesajı döndürüyoruz.
        return jsonify({'error': f'Veriler çekilirken hata oluştu: {str(e)}'}), 500

# Flask uygulamasını çalıştırıyoruz.
if __name__ == '__main__':
    app.run(debug=True)
