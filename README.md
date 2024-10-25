# JsonLand

JsonLand, JSON verilerini formatlama, kaçış karakterlerini kaldırma, Unicode karakterlerini çözme, SQL `INSERT` sorgularına dönüştürme ve SQL `INSERT` sorgularını JSON verilerine dönüştürme işlemleri sunan Python tabanlı, kaliteli ve inovatif araçlar topluluğudur.

## Özellikler

- **JSON to SQL Dönüştürme (`jts`)**: JSON nesnelerini SQL `INSERT` sorgularına dönüştürür.
- **SQL to JSON Dönüştürme (`stj`)**: SQL `INSERT` sorgularını JSON nesnelerine dönüştürür.
- **JSON Formatlama (`format`)**: JSON verisini daha okunabilir hale getirir.
- **Kaçış Karakterlerini Kaldırma (`remove-slashes`)**: JSON içindeki kaçış karakterlerini (`\`) temizler.
- **Unicode Kaçışlarını Kaldırma (`unescaped-unicode`)**: JSON içindeki Unicode kaçış karakterlerini çözer.

## Kurulum

1. **Depoyu klonlayın:**

   ```bash
   git clone https://github.com/kullanici_adi/JsonLand.git
   cd JsonLand
   ```
2. **Gerekli paketleri yükleyin:**

   ```bash
   pip install -r requirements.txt
   ```
3. **Aracı kurulum için yükleyin:**

   ```bash
   pip install .
   ```

   Bu adım, `jsonland` komutunu doğrudan kullanabilmenizi sağlar.

## Kullanım

JsonLand, iki ana işlevi destekler: `jts` (JSON to SQL) ve `stj` (SQL to JSON). Ek olarak, JSON verisini işlerken `format`, `remove-slashes` ve `unescaped-unicode` gibi işlemleri uygulayabilirsiniz.

### Genel Komut Yapısı

```bash
jsonland -d <dönüşüm_yönü> -json <json_dosyası> -sql <sql_dosyası> -table <tablo_adı> [-o <işlemler>]
```
