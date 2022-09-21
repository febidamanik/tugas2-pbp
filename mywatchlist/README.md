# 📑TUGAS-3 PBP📑

Nama  	: Febi Claudia Damanik

NPM	: 2106751884

Kelas 	: D

<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
</head>
<body>
 <table>
 	<tr>
 		<td>🔗Link HTML</td>
 		<td>https://tugas2-pbp-febidamanik.herokuapp.com/mywatchlist/html/</td>
 	</tr>
 	<tr>
 		<td>🔗Link JSON</td>
 		<td>https://tugas2-pbp-febidamanik.herokuapp.com/mywatchlist/json/</td>
  	<tr>
   	<td>🔗Link XML</td>
    <td>https://tugas2-pbp-febidamanik.herokuapp.com/mywatchlist/xml/</td>
   </tr>
 </table>

</body>
</html>

# 🔍Perbedaan JSON, XML, dan HTML🔍
▫ JSON (JavaScript Object Notation) merupakan sebuah format berbasis notasi objek dalam Javascript yang menerjemahkan bahasa pemrograman digunakan dalam transfer dan penyimpanan data serta menukar informasi dari web server sehingga dapat ditampilkan pada halaman web.

Contoh: 
```
{
  "first_name" : "Febi",
  "last_name" : "Damanik",
}
```
▫ XML (Extensible Markup Language) merupakan bahasa markup yang menyederhanakan proses pertukaran dan penyimpanan data dari suatu aplikasi ke aplikasi lain melalui internet.

Contoh: 
```<?xml version="1.0"?>
<listFilm>
    <film>
</listFilm>
```
▫ HTML (Hypertext Markup Language) merupakan bahasa markup standar yang digunakan untuk membuat serta menampilkan data pada halaman website dan aplikasi web.

Contoh: 
```
  <h3 style="text-align: left; color: #00294f">Name: {{nama}}</h3>
```

# 📩Mengapa perlu Data delivery?📩
Perubahan data yang dinamis membuat aplikasi membutuhkan cara bagaimana agar dapat menyimpan data dari user ke dalam database dengan cepat. Hal ini dapat dilakukan dengan pemrosesan data secara masif sehingga diperlukan data delivery yang akan menjadi mengambil data yang diperoleh dari database kemudian ditampilkan di sisi server situs atau aplikasi. Dengan begitu, pentingnya data perantara untuk pertukaran data, seperti JSON dan XML. Melalui perantara ini, akan memudahkan user dan server dalam pengambilan data ke bagian backend dengan cepat.

# 📌Pengimplementasian checklists dari tasks📌
▫ Membuat django-app dengan 'startnewapp' diberi nama mywatchlist dengan command berikut.
```
python manage.py startapp wishlist
```
▫ Menambahkan path aplikasi mywatchlist ke dalam 'urls.py' di project_django dan mywatchlist.
```
urlpatterns = [
    ...
    path('mywatchlist/', include('mywatchlist.urls')),
]
```
▫ Membuat models dengan properti 'watched', 'title', 'rating', 'release_date', dan 'review'.
```
class MyWatchList(models.Model):
    watched = models.BooleanField() 
    title = models.TextField()
    rating = models.IntegerField()
    release_date = models.DateField()
    review = models.TextField()
```
▫ Menyiapkan migrasi skema model ke dalam database Django lokal.
```
python manage.py makemigrations
```
▫ Membuat folder fixtures berisi file json yang di dalamnya memuat daftar film dilanjutkan dengan melakukan loaddata untuk menyimpan isinya ke database.
```[
    {
    "model": "mywatchlist.mywatchlist",
    "pk": 4,
    "fields":{
        "watched": false,
        "title":"Despicable Me",
        "rating": 4,
        "release_date": "2010-07-09",
        "review":"This movie has a beautifully animated and boasts some standout talent"

    }
},...
```
▫ Membuat fungsi 'show_mywatchlist', 'show_mywatchlist_json', dan 'show_mywatchlist_xml'. 
▫ Menambahkan potongan kode untuk melakukan loaddata pada fixtures dari aplikasi mywatchlist yang akhirnya di-deploy ke Herokuapp.

# 🖨Hasil Screenshot Postman🖨
▫ **HTML**
http://localhost:8000/mywatchlist/html untuk mengakses mywatchlist dalam format HTML

![image](https://user-images.githubusercontent.com/112416751/191333281-ff9936ef-9a85-4eb2-8cea-76ba6c581637.png)

▫ **JSON**
 http://localhost:8000/mywatchlist/json untuk mengakses mywatchlist dalam format JSON
 
![image](https://user-images.githubusercontent.com/112416751/191333476-d0fb8bce-bd05-4403-a32c-c9ec7e1fb4ea.png)

▫ **XML**
 http://localhost:8000/mywatchlist/xml untuk mengakses mywatchlist dalam format XML
 
![image](https://user-images.githubusercontent.com/112416751/191334092-cf04cd55-9a01-479c-8a63-c7766c9358d3.png)
