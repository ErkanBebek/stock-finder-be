import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify
import asyncio
from pyppeteer import launch 

# Flask uygulamasını başlatıyoruz.
app = Flask(__name__)

# '/fetch-indices-data' URL'ine gelen GET isteklerini işleyecek bir rota tanımlıyoruz.
@app.route('/fetch-indices-data', methods=['GET'])
def fetch_indices_data():
    return asyncio.run(scrape_data())

async def scrape_data():
    url = 'https://finance.yahoo.com/world-indices/'

    try:
        # Puppeteer tarayıcısını başlatıyoruz.
        browser = await launch()
        page = await browser.newPage()
        # Belirtilen URL'ye gidiyoruz ve ağın durulmasını bekliyoruz.
        await page.goto(url, {'waitUntil': 'networkidle2'})

        # Sayfa içeriğini değerlendiriyoruz ve gerekli verileri çekiyoruz.
        stock_data = await page.evaluate('''
            () => {
                const rows = document.querySelectorAll('tr');
                const data = [];
                rows.forEach(row => {
                    const symbol = row.querySelector('[aria-label="Symbol"]')?.innerText || 'N/A';
                    const name = row.querySelector('[aria-label="Name"]')?.innerText || 'N/A';
                    const last = row.querySelector('[aria-label="Last Price"]')?.innerText || 'N/A';
                    const change = row.querySelector('[aria-label="Change"]')?.innerText || 'N/A';
                    const percentage_change = row.querySelector('[aria-label="% Change"]')?.innerText || 'N/A';
                    const volume = row.querySelector('[aria-label="Volume"]')?.innerText || 'N/A';

                    if (symbol !== 'N/A') {
                        data.push({ symbol, name, last, change, percentage_change, volume });
                    }
                });
                return data;
            }
        ''')

        # Tarayıcıyı kapatıyoruz.
        await browser.close()
        
        # JSON formatında hisse senedi verilerini döndürüyoruz.
        return jsonify({'stockData': stock_data}), 200
    except Exception as e:
        # Hata durumunda JSON formatında hata mesajı döndürüyoruz.
        return jsonify({'error': f'Veriler çekilirken hata oluştu: {str(e)}'}), 500

# Flask uygulamasını çalıştırıyoruz.
if __name__ == '__main__':
    app.run(debug=True)
