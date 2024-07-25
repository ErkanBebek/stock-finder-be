from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Stock
from .serializers import StockSerializer
from .models import Comment
from .serializers import CommentSerializer

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class CommentsByStockAPIView(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        stock_id = self.request.query_params.get('stock')
        if stock_id:
            return Comment.objects.filter(stock_id=stock_id)
        else:
            return Comment.objects.none()  # Or handle no stock parameter case

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    

# bruadan sonra çekme fonksiyonu

# import requests
# from bs4 import BeautifulSoup

# def scrape_data():
#     url = 'https://markets.businessinsider.com/indices'

#     try:
#         response = requests.get(url)
#         response.raise_for_status()  # Raise an exception for HTTP errors
#         html = response.text
#         soup = BeautifulSoup(html, 'html.parser')

#         stock_data = []
#         for row in soup.select('tbody>tr'):
#             symbol = row.select_one('a.deep-sea-blue').get('title')
#             if symbol:
#                 symbolcountry = row.find_all("td")[0].get_text(strip=True)
#                 last, prev_close = [td.get_text(strip=True) for td in row.select("td.text-right")[0].contents if td.name == 'br']
#                 balance = row.select_one("td.text-right span").get_text(strip=True)
#                 percentage_change = row.select("td.text-right")[1].get_text(strip=True).split("\n")[1]
#                 time = row.select("td.text-right")[2].select_one("span").get_text(strip=True)
#                 date = row.select("td.text-right")[2].get_text(strip=True).split("\n")[1]
#                 ytd, one_year = row.select("td.text-right")[-1].get_text(strip=True).split("\n")

#                 stock_data.append({
#                     'symbol': symbol,
#                     'symbolcountry': symbolcountry,
#                     'last': last,
#                     'prev_close': prev_close,
#                     'balance': balance,
#                     'percentage_change': percentage_change,
#                     'time': time,
#                     'date': date,
#                     'ytd': ytd,
#                     'one_year': one_year
#                 })

#         return stock_data

#     except requests.RequestException as e:
#         return {'error': f'An error occurred while fetching data: {e}'}

# # Usage
# data = scrape_data()
# if 'error' in data:
#     print(data['error'])
# else:
#     for stock in data:
#         print(stock)
