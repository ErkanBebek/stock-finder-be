import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify
from db import get_db_connection

def get_bist_database_joiner():
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
        connection = get_db_connection()
        cursor = connection.cursor()
        
        
        stock_data = []
        # '.live-stock-item' sınıfına sahip tüm HTML elemanlarını seçiyoruz.
        for item in soup.select('.live-stock-item'):
            # Her bir hisse senedi elemanından gerekli verileri çekiyoruz.
            symbol = item.select('a')[1].text
            name_array = item.select('a')[1]['href'].split('/')[3][0:-6].split('-')
            name = name_array
            if len(name_array) >4:
                name = name_array[-4].capitalize()+" "+name_array[-3].capitalize()+" "+name_array[-2].capitalize()+" "+name_array[-1].capitalize()
            elif len(name_array) >3:
                name = name_array[-3].capitalize()+" "+name_array[-2].capitalize()+" "+name_array[-1].capitalize()
            elif len(name_array) >2:
                name = name_array[-2].capitalize()+" "+name_array[-1].capitalize()
            else:
                name = name_array[1].capitalize()
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
                'symbol': symbol,
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
            cursor.execute(
            "INSERT INTO tr_stock (symbol, name) VALUES ( %s,%s)",
            (symbol,name)
            )
        connection.commit()
        cursor.close()
        connection.close()

        return stock_data
    except Exception as e:
        # Hata durumunda JSON formatında hata mesajı döndürüyoruz.
        return jsonify({'error': f'Veriler çekilirken hata oluştu: {str(e)}'}), 500


def get_dow_jones_database_joiner():
    url = "https://tr.tradingview.com/symbols/DJ-DJI/components/"
    try:
        
        stock_data_total = []
        connection = get_db_connection()
        cursor = connection.cursor()
    
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
                volume = cells[5].text 
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

                print(icon_src)  # Print either the src attribute or "NaN"

                   

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
                    'div_yield':div_yield

                  
                })
                cursor.execute(
                "INSERT INTO us_stock (symbol, name) VALUES ( %s,%s)",
                (symbol,name)
                )
        connection.commit()
        cursor.close()
        connection.close()

        #print({'stockData': stock_data_total})
        # JSON formatında hisse senedi verilerini döndürüyoruz.
        return {'stockData': stock_data_total}
    except Exception as e:
        # Hata durumunda JSON formatında hata mesajı döndürüyoruz.
        return {'error': f'Veriler çekilirken hata oluştu: {str(e)}'}, 500

def get_cryptocurrencies_database_joiner():
    url = "https://tr.tradingview.com/markets/cryptocurrencies/prices-all"
    try:
        
        stock_data_total = []

        connection = get_db_connection()
        cursor = connection.cursor()
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

                print(icon_src)  # Print either the src attribute or "NaN"

                   

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
                    'change':change
                  
                })
                cursor.execute(
                "INSERT INTO global_coins (symbol, name) VALUES ( %s,%s)",
                (symbol,name)
                )
        connection.commit()
        cursor.close()
        connection.close()

        #print({'stockData': stock_data_total})
        # JSON formatında hisse senedi verilerini döndürüyoruz.
        return {'stockData': stock_data_total}
    except Exception as e:
        # Hata durumunda JSON formatında hata mesajı döndürüyoruz.
        return {'error': f'Veriler çekilirken hata oluştu: {str(e)}'}, 500
