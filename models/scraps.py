import requests
import asyncio
from bs4 import BeautifulSoup
from flask import Flask, jsonify
#https://tr.tradingview.com/markets/stocks-turkey/market-movers-large-cap/

def get_bist_data():
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
            name = item.select('a')[1].text
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
        return stock_data
    except Exception as e:
        # Hata durumunda JSON formatında hata mesajı döndürüyoruz.
        return jsonify({'error': f'Veriler çekilirken hata oluştu: {str(e)}'}), 500

def get_economic_calendar_data():
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
        return {'dates': data}
    except Exception as e:
        # Hata durumunda JSON formatında hata mesajı döndürüyoruz.
        return jsonify({'error': f'Veriler çekilirken hata oluştu: {str(e)}'}), 500

def get_global_index_data():
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
            symbolcountry = row.select_one('td').decode_contents().split("<br/>")[1].strip()
            print(symbolcountry)
            
            # Son fiyatı çekme
            last = row.select('td.text-right')[0].decode_contents().split("<br/>")[0].strip()
            print(last)
            
            # Önceki kapanış fiyatını çekme
            prev_close = row.select('td.text-right')[0].decode_contents().split("<br/>")[1].strip()
            print(prev_close)
            
            # Denge bilgisini çekme
            balance =  row.select('td.text-right')[1].text.strip().split("\n")[0]
            print(balance)
            
            # Yüzde değişim bilgisini çekme
            percentage_change = row.select('td.text-right')[1].text.strip().split("\n")[1]
            print(percentage_change)
            
            # Zaman bilgisini çekme
            time = row.select('td.text-right')[2].find('span').text
            print(time)
            
            # Tarih bilgisini çekme
            date = row.select('td.text-right')[2].text.strip().split("\n")[1]
            print(date)

            # Yıl başından bugüne değişim bilgisini çekme
            ytd = row.select('td.text-right')[-1].text.strip().split("\n")[0]
            print(ytd)

            # Bir yıllık değişim bilgisini çekme
            one_year = row.select('td.text-right')[-1].text.strip().split("\n")[1]
            print(one_year)

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
        return {'stockData': stock_data}
    except Exception as e:
        # Hata durumunda JSON formatında hata mesajı döndürüyoruz.
        return jsonify({'error': f'Veriler çekilirken hata oluştu: {str(e)}'}), 500


#bir ara bak
# def get_nasdaq_100_data():
#     try:
#         urls = [
#             'https://markets.businessinsider.com/index/nasdaq_100?p=1',
#             'https://markets.businessinsider.com/index/nasdaq_100?p=2',
#             'https://markets.businessinsider.com/index/nasdaq_100?p=3',
#         ]
#         stock_data_total = []

#         for url in urls:
#             # Belirtilen URL'ye HTTP GET isteği gönderiyoruz.
#             response = requests.get(url)
#             # İsteğin başarılı olup olmadığını kontrol ediyoruz.
#             response.raise_for_status()
#             # Gelen HTML içeriğini alıyoruz.
#             html = response.content
#             # BeautifulSoup ile HTML içeriğini ayrıştırıyoruz.
#             soup = BeautifulSoup(html, 'html.parser')

            
#             rows = soup.find_all('tr', class_='table__tr')

#             # Her satırdan (tr) verileri çıkarın
#             for row in rows:
#                 # İlgili td elementlerini seçin
#                 cells = asyncio.row.find_all('td', class_='table__td')

#                 if len(cells) >= 5:
#                     # Her hücreden (td) veriyi çekin
#                     symbol = cells[0].find('a').text.strip() if cells[0].find('a') else "bulunamadı"
#                     last = cells[1].text.strip() if cells[1] else "bulunamadı"
#                     prev_close = cells[2].find('span').text.strip() if cells[2].find('span') else "bulunamadı"
#                     percentage_change = cells[3].find('span').text.strip() if cells[3].find('span') else "bulunamadı"
#                     balance = cells[4].find('span').text.strip() if cells[4].find('span') else "bulunamadı"
#                     time = cells[5].find('span').text.strip() if cells[5].find('span') else "bulunamadı"

                    

#                     stock_data_total.append({
#                         'symbol': symbol,
#                         'last': last,
#                         'prev_close': prev_close,
#                         'balance': balance,
#                         'percentage_change': percentage_change,
#                         'time': time,
#                     })

#         print({'stockData': stock_data_total})
#         # JSON formatında hisse senedi verilerini döndürüyoruz.
#         return {'stockData': stock_data_total}
#     except Exception as e:
#         # Hata durumunda JSON formatında hata mesajı döndürüyoruz.
#         return {'error': f'Veriler çekilirken hata oluştu: {str(e)}'}, 500


#https://markets.businessinsider.com/index/dow_jones
def get_dow_jones_30_data():
    url = "https://tr.tradingview.com/symbols/DJ-DJI/components/"
    try:
        
        stock_data_total = []

    
        # Belirtilen URL'ye HTTP GET isteği gönderiyoruz.
        response = requests.get(url)
        # İsteğin başarılı olup olmadığını kontrol ediyoruz.
        response.raise_for_status()
        # Gelen HTML içeriğini alıyoruz.
        html = response.content
        # BeautifulSoup ile HTML içeriğini ayrıştırıyoruz.
        soup = BeautifulSoup(html, 'html.parser')


        table = soup.find("table", class_="table-Ngq2xrcG")
        # print("table:",table.decode_contents)
        rows = table.find_all('tr', class_='row-RdUXZpkv')

        # Her satırdan (tr) verileri çıkarın
        for row in rows:
            # İlgili td elementlerini seçin
            cells = row.find_all('td', class_='cell-RLhfr_y4')

            if len(cells) >= 5:
                # Her hücreden (td) veriyi çekin
                symbol = cells[0].find("a").text
                # print(symbol)
                name = cells[0].find("sup").text
                # print(name)
                market_cap = cells[1].text[:-6] 
                # print(order)
                price = cells[2].text[:-4] 
                change = cells[3].text
                volume = cells[4].text 
                percentage_volume = cells[5].text 
                p_e = cells[6].text
                eps_dil = cells[7].text
                eps_dil_growt = cells[8].text
                div_yield = cells[9].text
                sector = cells[10].text
                icon = cells[0].find("img") if cells[0] else None  # Find img element, assign None if cell doesn't exist
                if icon:  # Check if img element was found (not None)
                    icon_src = icon['src']
                else:
                    icon_src = "NaN"  # Assign NaN if no image found

                # print(icon_src)  # Print either the src attribute or "NaN"

                   

                stock_data_total.append({
                    'symbol': symbol,
                    'name':name,
                    'price':price,
                    'icon_src': icon_src,
                    'market_cap': market_cap,
                    'volume': volume,
                    'p_e': p_e,
                    'sector': sector,
                    'change':change,
                    'eps_dil':eps_dil,
                    'eps_dil_growt':eps_dil_growt,
                    'div_yield':div_yield,
                    'percentage_volume':percentage_volume,
                    'locale':"US"                 
                })

        #print({'stockData': stock_data_total})
        # JSON formatında hisse senedi verilerini döndürüyoruz.
        return {'stockData': stock_data_total}
    except Exception as e:
        # Hata durumunda JSON formatında hata mesajı döndürüyoruz.
        return {'error': f'Veriler çekilirken hata oluştu: {str(e)}'}, 500
    
    
def get_bist_XU100_data():
    url = "https://www.tradingview.com/symbols/BIST-XU100/components/"
    try:
        
        stock_data_total = []

    
        # Belirtilen URL'ye HTTP GET isteği gönderiyoruz.
        response = requests.get(url)
        # İsteğin başarılı olup olmadığını kontrol ediyoruz.
        response.raise_for_status()
        # Gelen HTML içeriğini alıyoruz.
        html = response.content
        # BeautifulSoup ile HTML içeriğini ayrıştırıyoruz.
        soup = BeautifulSoup(html, 'html.parser')


        table = soup.find("table", class_="table-Ngq2xrcG")
        # print("table:",table.decode_contents)
        rows = table.find_all('tr', class_='row-RdUXZpkv')

        # Her satırdan (tr) verileri çıkarın
        for row in rows:
            # İlgili td elementlerini seçin
            cells = row.find_all('td', class_='cell-RLhfr_y4')

            if len(cells) >= 5:
                # Her hücreden (td) veriyi çekin
                symbol = cells[0].find("a").text
                # print(symbol)
                name = cells[0].find("sup").text
                # print(name)
                market_cap = cells[1].text[:-6] 
                # print(order)
                price = cells[2].text[:-4] 
                change = cells[3].text
                volume = cells[4].text 
                percentage_volume = cells[5].text 
                p_e = cells[6].text
                eps_dil = cells[7].text
                eps_dil_growt = cells[8].text
                div_yield = cells[9].text
                sector = cells[10].text
                icon = cells[0].find("img") if cells[0] else None  # Find img element, assign None if cell doesn't exist
                if icon:  # Check if img element was found (not None)
                    icon_src = icon['src']
                else:
                    icon_src = "NaN"  # Assign NaN if no image found

                # print(icon_src)  # Print either the src attribute or "NaN"

                   

                stock_data_total.append({
                    'symbol': symbol,
                    'name':name,
                    'price':price,
                    'icon_src': icon_src,
                    'market_cap': market_cap,
                    'volume': volume,
                    'p_e': p_e,
                    'sector': sector,
                    'change':change,
                    'eps_dil':eps_dil,
                    'eps_dil_growt':eps_dil_growt,
                    'div_yield':div_yield,
                    'percentage_volume':percentage_volume,
                    'locale':"TR"                 
                                      
                })

        #print({'stockData': stock_data_total})
        # JSON formatında hisse senedi verilerini döndürüyoruz.
        return {'stockData': stock_data_total}
    except Exception as e:
        # Hata durumunda JSON formatında hata mesajı döndürüyoruz.
        return {'error': f'Veriler çekilirken hata oluştu: {str(e)}'}, 500



def get_cryptocurrencies_data():
    url = "https://tr.tradingview.com/markets/cryptocurrencies/prices-all"
    try:
        
        stock_data_total = []

    
        # Belirtilen URL'ye HTTP GET isteği gönderiyoruz.
        response = requests.get(url)
        # İsteğin başarılı olup olmadığını kontrol ediyoruz.
        response.raise_for_status()
        # Gelen HTML içeriğini alıyoruz.
        html = response.content
        # BeautifulSoup ile HTML içeriğini ayrıştırıyoruz.
        soup = BeautifulSoup(html, 'html.parser')


        table = soup.find("table", class_="table-Ngq2xrcG")
        # print("table:",table.decode_contents)
        rows = table.find_all('tr', class_='row-RdUXZpkv')

        # Her satırdan (tr) verileri çıkarın
        for row in rows:
            # İlgili td elementlerini seçin
            cells = row.find_all('td', class_='cell-RLhfr_y4')

            if len(cells) >= 5:
                # Her hücreden (td) veriyi çekin
                symbol = cells[0].find("a").text
                # print(symbol)
                name = cells[0].find("sup").text
                # print(name)
                order = cells[1].text
                # print(order)
                price = cells[2].text[:-4] 
                change = cells[3].text
                market_cap = cells[4].text[:-4] 
                volume = cells[5].text[:-4] 
                circ_supply = cells[6].text
                category = cells[7].text
                icon = cells[0].find("img") if cells[0] else None  # Find img element, assign None if cell doesn't exist
                if icon:  # Check if img element was found (not None)
                    icon_src = icon['src']
                else:
                    icon_src = "NaN"  # Assign NaN if no image found

                # print(icon_src)  # Print either the src attribute or "NaN"

                   

                stock_data_total.append({
                    'symbol': symbol,
                    'name':name,
                    'order':order,
                    'price':price,
                    'icon_src': icon_src,
                    'market_cap': market_cap,
                    'volume': volume,
                    'circ_supply': circ_supply,
                    'category': category,
                    'change':change,
                    'locale':"WORLD"                 
                  
                })

        #print({'stockData': stock_data_total})
        # JSON formatında hisse senedi verilerini döndürüyoruz.
        return {'stockData': stock_data_total}
    except Exception as e:
        # Hata durumunda JSON formatında hata mesajı döndürüyoruz.
        return {'error': f'Veriler çekilirken hata oluştu: {str(e)}'}, 500

