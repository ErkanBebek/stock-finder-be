| Dosya adı   | Alan Adı                         | Veri Tipi | Uzunluk | Açıklama                                |
|-------------|----------------------------------|-----------|---------|-----------------------------------------|
| users       | ID                               | int       | 4       | kullanıcı no                            |
|             | username                         | varchar   | 20      | kullanıcı adı                           |
|             | password                         | varchar   | 14      | şifre                                   |
|             | email                            | varchar   | 20      | kullanıcı e-mail adresi                 |
|             | role                             | varchar   | 10      | yetki seviyesi                          |
|             | name                             | varchar   | 20      | Kullanıcı adı                 |
|             | surname                          | varchar   | 20      | Kullanıcı soyadı                 |
|             | phone                            | varchar   | 20      | Kullanıcı soyadı                 |
| us_stock    | ID                               | int       | 4       | kullanıcı no                            |
|             | symbol                           | varchar   | 20      | hisse senedi sembolü                    |
| tr_stock    | ID                               | int       | 4       | kullanıcı no                            |
|             | symbol                           | varchar   | 20      | hisse senedi sembolü                    |
| global_coins    | ID                               | int       | 4       | kullanıcı no                            |
|             | symbol                           | varchar   | 20      | kripto para adı                    |
| tr_stock_fundamentals    | ID                               | int       | 4       | id                                      |
|             | stock_name                 | varchar   | 100     | hisse senedi adı                        |
|             | last_price                        | double    |         | son fiyat                               |
|             | profit_change                      | double    |         | kar değişimi                            |
|             | last_period_profit                    | double    |         | son dönem kar                           |
|             | last_year_profit                   | double    |         | geçen sene kar                          |
|             | last_period                        | text      |         | son dönem                               |
|             | ev_ebitda                         | double    |         | FD/ FAVÖK                               |
|             | sector_ev_ebitda_average     | double    |         | sektörün FD/ FAVÖK Ortalaması           |
|             | ev_sales                      | double    |         | FD/ Satışlar                            |
|             | sector_ev_sales_average  | double    |         | sektörün FD/ Satışlar Ortalaması        |
|             | pe_ratio                               | double    |         | F/K                                     |
|             | sector_pe_ratio_average           | double    |         | sektörün FK Ortalaması                  |
|             | pbv_ratio                            | double    |         | PD/DD                                   |
|             | sector_pbv_ratio_average        | double    |         | sektörün PD/DD Ortalaması               |
|             | sector                           | text      |         | sektör                                  |
| comments    | ID                               | int       | 4       | yorum no                                |
|             | stock_id                         | int       | 4       | ilgili hisse ID                         |
|             | stock_locale                         | int       | 4       | ilgili hisse ülkesi ID                         |
|             | user_id                          | int       | 4       | yorum yapan kullanıcı ID                |
|             | comment                          | text      |         | yorum metni                             |
|             | created_at                       | datetime  |         | yorumun oluşturulma tarihi              |
|             | updated_at                       | datetime  |         | yorumun güncellenme tarihi              |
| contact_message    | ID                               | int       | 4       | mesaj no                                |
|             | user_id                          | int       | 4       | mesaj atan kullanıcı ID                |
|             | reciever_id                          | int       | 4       | mesajı alacak kullanıcı ID                |
|             | message                          | text      |         | mesaj metni                             |
|             | created_at                       | datetime  |         | yorumun oluşturulma tarihi              |
|             | updated_at                       | datetime  |         | yorumun güncellenme tarihi              |
| user_stock_entry   | ID                               | int       | 4       | yorum no                                |
|             | user_id                          | int       | 4       | hisse alan kullanıcı ID                |
|             | stock_id                         | int       | 4       | ilgili hisse ID                         |
|             | stock_locale                         | varchar       | 255       | ilgili hisse ülkesi ID                         |
|             | snapshot_price                          | double      |         | hissenin satın alındığı fiyat                             |
|             | sold_price                          | double      |         | hissenin satıldığı fiyat                             |
|             | buy_date                       | datetime  |         | alım emri oluşturulma tarihi              |
|             | sell_date                       | datetime  |         | satım emri  tarihi              |
