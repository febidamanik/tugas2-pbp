# 📑TUGAS-6 PBP📑

**Tugas 6: Javascript dan AJAX**

Nama	: Febi Claudia Damanik

NPM	: 2106751884

Kelas 	: D

# 🔗Link🔗
https://tugas2-pbp-febidamanik.herokuapp.com/todolist/

# 🔎Asynchronous programming VS Synchronous programming🔎
Metode asynchronous programming dan synchronous programming merupakan suatu metode yang digunakan dalam konteks programming yang memiliki perbedaan serta keunggulan dan kekurangannya masing-masing.

Asynchronous programming

➔ Pendekatan pemrograman yang tidak terikat pada input/output (I/O). Program dapat berjalan secara paralel tanpa adanya `blocking` sehingga dapat mengirim `multiple request` ke server. 

Synchronus programming

➔ Pendekatan pemrograman yang lebih `old style`. Program hanya dapat mengeksekusi baris program satu per satu sesuai dengan urutan dan prioritas task.

Berikut tabel yang menampilkan perbedaan antara keduanya.
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
</head>
<body> 
 <table>
 	<tr>
 		<td>📴Asynchronous programming</td>
 		<td>📲Synchronous programming</td>
 	<tr>
 		<td>Multi-thread</td>
 		<td>Single-thread</td>
  <tr>
		<td>Berjalan secara paralel</td>
		<td>Berjalan secara sequential</td>
  <tr>
		<td>Non blocking, dapat mengirim multiple request ke server</td>
		<td>Blocking, hanya dapat mengirim request jika request sebelumnya sudah 		 selesai </td>
  <tr>
		<td>Durasi eksekusi lebih singkat dan cepat</td>
		<td>Durasi eksekusi bergantung dengan task lain</td>
  <tr>
		<td>Mengeksekusi task tanpa terikat dengan proses lain</td>
		<td>Mengeksekusi task sekaligus menunggu task lain untuk diproses</td>
   </tr>
	 
 </table>

</body>
</html>

# 🤷‍♂️Penerapan paradigma Event-Driven Programming🤷‍♂️
*Event-Driven Programming* adalah suatu paradigma dimana konsep kerjanya berkomunikasi secara tidak langsung dengan sebuah perantara yang menghubungkan entitas satu dengan yang lainnya. Dengan begitu, pada saat pengguna melakukan interaksi maka akan terjadi suatu *event* dimana juga terdapat kode JavaScript yang *running* untuk menampilkan *event* yang terjadi serta melakukan perubahan pada halaman.
Contoh: 
Pada saat, menekan button “Login” maka akan menyebabkan sebuah event terjadi, yaitu akan muncul pemanggilan fungsi hello() pada halaman website.
Berikut kode dari untuk menampilkan contoh di atas.
```html
<button onclick=”hello()”>Login</button>
```
# 👩‍💻Penerapan asynchronous programming pada AJAX👩‍💻
Penerapan tersebut terjadi ketika adanya *event* yang dijalankan pada halaman website. Seperti yang telah dibahas sebelumnya pada contoh *Event-Driven Programming*, maka JavaScript AJAX akan mengirimkan sebuah *request* ke server yang akan mengakses suatu URL untuk menampilkan halaman sesuai dengan *request* yang diberikan. Selain itu, *asynchronous programming* pada AJAX dapat mengirimkan dan menerima data dari server tanpa harus me-reload keseluruhan halaman website sehingga proses dapat bekerja secara bersamaan tanpa mengganggu fungsi masing-masing.
Berikut langkah-langkah dalam penerapannya.
- Menambahkan AJAX di awal program dengan memberikan tag `<scripts>` diakhir dengan `</scripts>`
- Menambahkan library AJAX di dalam tag `<head>` 
```html
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
```
- Pada fitur program yang diinginkan tambahkan program AJAX di dalam tag tersebut `$.ajax({...})`
- Event dari user akan diproses ke AJAX saat user mengirimkan event tertentu pada server.
- Melakukan transfer data dan menampung segala *event* yang dikirimkan untuk kemudian diproses oleh AJAX
- Dengan metode *asynchronous programming*, data yang berasal dari pengguna akan diproses secara *server-side scripting* dimana pengolahan datanya dilakukan oleh komputer server/penyedia
- Hasil dari pengolahan data ini kemudian akan ditampilkan pada halaman website secara langsung dengan data baru di dalamnya
- Menerapkan GET dan POST untuk mengakses, mengedit, dan mengirimkan data dari JSON ke server.
# 📌Pengimplementasian checklists dari tasks📌
◽ Membuat fungsi show_json pada view yang mengembalikan seluruh data task dalam bentuk JSON kemudian mengembalikan request pada file todolist_ajax.html
html```
def show_json(request):
    data = Task.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')
    ```
    
◽ Menambahkan `path('json/', show_json, name='show-json')` ke dalam URL patterns di file urls.py pada folder todolist

◽ Menambahkan modal menggunakan Bootstrap untuk menampung input data dalam format form dari user yang akan dimasukkan ke database pada todolist_ajax.html 

◽ Menerapkan AJAX GET untuk menampilkan data di halaman website dengan membuat tag script berisi JavaScript. 

◽ Pada fungsi `getData();` akan dikembalikan data JSON dari list user dimana data tersebut menjadi argumen show_data

◽ Pada kode `$(document).ready(function(){})` akan dipanggil getData untuk memperbarui halaman website secara asinkronus

◽ Menghubungkan tombol Add Task untuk membuka modal dalam format form dengan fungsi `create_task()` 

◽ Menambahkan `path('add/', create_task_ajax, name='create-task-ajax')` pada `urlpatterns = []` di urls.py

◽ Membuat fungsi `clearFields()` pada tag `<script>` di todolist.html untuk menghapus isi dari fields pada modal.

◽ Melakukan refresh pada halaman utama secara asinkronus untuk menampilkan list terbaru tanpa reload seluruh halaman

◽ Membuat routing agar fungsi dapat kita buka melalui localhost dan memastikan sudah terdeploy ke herokuapp menggunakan repository tugas sebelumnya

◻Tambahan Implementasi Bonus◻

◽ ☑ Mengimplementasikan AJAX DELETE untuk setiap button delete pada card dengan fungsi `deleteData(id){}` pada file todolist untuk memanggil `endpoint` dari penghapusan task
◽ ☑ Membuat view baru dengan menghapus task sesuai dengan ID tertentu

◽ ☑ Membuat kolom baru pada task dengan tombol Hapus

◽ ☑ Membuat view baru yang menghapus task dengan ID tertentu

◽ ☑ Membuat path `/todolist/delete/{id}` yang menerima ID dari path dan meneruskannya kepada view

◽ ☑ Membuat fungsi JavaScript yang memanggil endpoint penghapusan task

◽ ☑ Melakukan refresh pada halaman utama secara asinkronus untuk menampilkan list terbaru tanpa reload seluruh halaman

