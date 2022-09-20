# 📑TUGAS-3 PBP📑

Nama  : Febi Claudia Damanik

NPM   : 2106751884

Kelas : D

[**🔗Link HTML**](https://tugas2-pbp-febidamanik.herokuapp.com/mywatchlist/html/)

[**🔗Link JSON**](https://tugas2-pbp-febidamanik.herokuapp.com/mywatchlist/json/)

[**🔗Link XML**](https://tugas2-pbp-febidamanik.herokuapp.com/mywatchlist/xml/)

# 🔍Perbedaan JSON, XML, dan HTML🔍
▫ JSON (JavaScript Object Notation) merupakan sebuah format yang menerjemahkan bahasa pemrograman digunakan dalam transfer dan penyimpanan data serta menukar informasi dari web server sehingga dapat ditampilkan pada halaman web.

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
Perubahan data yang dinamis membuat aplikasi membutuhkan cara bagaimana agar dapat menyimpan data dari user ke dalam database dengan cepat. Hal ini dapat dilakukan dengan pemrosesan data secara masif sehingga diperlukan HTTP Protocols yang akan membantu developer melakukan pengiriman data dengan menggunakan method, seperti get, post, patch, dan delete. Dengan begitu, pentingnya data perantara untuk pertukaran data, seperti JSON dan XML. Melalui perantara ini, akan memudahkan user dan server dalam pengambilan data ke bagian backend dengan cepat. Dengan HTTP Protocols akan membantu developer untuk melakukan pengiriman data untuk menerima perintah dari suatu frontend tentang pemrosesan suatu data.

# 📌Pengimplementasian checklists dari tasks📌
▫ Membuat django-app dengan 'startnewapp' kemudian tugas 2 diberi nama mywatchlist.

▫ Menambahkan path aplikasi mywatchlist ke dalam 'urls.py' di project_django dan mywatchlist.

▫ Membuat models dengan properti 'watched', 'title', 'rating', 'release_date', dan 'review'.

▫ Menyiapkan migrasi skema model ke dalam database Django lokal.

▫ Membuat folder fixtures berisi file json yang di dalamnya memuat daftar film dilanjutkan dengan melakukan loaddata untuk menyimpan isinya ke database.

▫ Membuat fungsi 'show_mywatchlist', 'show_mywatchlist_json', dan 'show_mywatchlist_xml'. 

▫ Menambahkan potongan kode untuk melakukan loaddata pada fixtures dari aplikasi mywatchlist yang akhirnya di-deply ke Herokuapp.

# 💻Hasil Screenshot Postman💻
▫ 
▫ 
▫ 

