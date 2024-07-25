from django.db import models

class Stock(models.Model):
    hisse_senedi_adi = models.TextField()
    son_fiyat = models.FloatField(null=True, blank=True)
    kar_degisim = models.FloatField(null=True, blank=True)
    son_donem_kar = models.FloatField(null=True, blank=True)
    gecen_sene_kar = models.FloatField(null=True, blank=True)
    son_donem = models.TextField()
    fd_favok = models.FloatField(null=True, blank=True)
    sektorun_fd_favok_ortalamasi = models.FloatField(null=True, blank=True)
    fd_satislar = models.FloatField(null=True, blank=True)
    sektorun_fd_satislar_ortalamasi = models.FloatField(null=True, blank=True)
    fk = models.FloatField(null=True, blank=True)
    sektorun_fk_ortalamasi = models.FloatField(null=True, blank=True)
    pd_dd = models.FloatField(null=True, blank=True)
    sektorun_pd_dd_ortalamasi = models.FloatField(null=True, blank=True)
    sektor = models.TextField()

    class Meta:
        db_table = 'tr_stock'



class Stock(models.Model):
    hisse_senedi_adi = models.TextField()
    son_fiyat = models.FloatField(null=True, blank=True)
    kar_degisim = models.FloatField(null=True, blank=True)
    son_donem_kar = models.FloatField(null=True, blank=True)
    gecen_sene_kar = models.FloatField(null=True, blank=True)
    son_donem = models.TextField()
    fd_favok = models.FloatField(null=True, blank=True)
    sektorun_fd_favok_ortalamasi = models.FloatField(null=True, blank=True)
    fd_satislar = models.FloatField(null=True, blank=True)
    sektorun_fd_satislar_ortalamasi = models.FloatField(null=True, blank=True)
    fk = models.FloatField(null=True, blank=True)
    sektorun_fk_ortalamasi = models.FloatField(null=True, blank=True)
    pd_dd = models.FloatField(null=True, blank=True)
    sektorun_pd_dd_ortalamasi = models.FloatField(null=True, blank=True)
    sektor = models.TextField()

    class Meta:
        db_table = 'tr_stock'



class Comment(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    comment_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'comments'

class User(models.Model):
    # name = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    roles = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.surname}"


    class Meta:
        db_table = 'users'