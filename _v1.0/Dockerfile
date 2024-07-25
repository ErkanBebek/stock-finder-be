# Python 3.9-alpine image kullanarak başlıyoruz
FROM python:3.12-alpine

# Çalışma dizinini oluştur
WORKDIR /app

# Gerekli sistem bağımlılıklarını yükle
RUN apk add --no-cache --virtual .build-deps \
    gcc musl-dev libffi-dev openssl-dev \
    mariadb-dev \
    && apk add --no-cache bash

# Gereken Python bağımlılıklarını yükle
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyalarını kopyala
COPY . /app/

# Gerekli dosya izinlerini ayarla
RUN chmod +x /app/manage.py

# # Gerekli Django komutlarını çalıştır
# RUN python manage.py makemigrations stockapp
# RUN python manage.py migrate

# Gereksiz bağımlılıkları temizle
# RUN apk del .build-deps

# # Gerekli ortam değişkenlerini ayarla
# ENV PYTHONUNBUFFERED=1


# Expose the necessary ports
EXPOSE 8000
EXPOSE 3307


# Uygulamanın sunucusunu başlat
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


## image build
# docker build -t mydjangoapp .
# docker run -p 8000:8000 -p 3307:3307 mydjangoapp

