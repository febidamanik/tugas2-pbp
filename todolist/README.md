# 📑TUGAS-4 PBP📑

Nama	: Febi Claudia Damanik

NPM	: 2106751884

Kelas 	: D

# 🔗Link🔗
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
</head>
<body>
 <table>
 	<tr>
 		<td>Halaman Utama</td>
 		<td>https://tugas2-pbp-febidamanik.herokuapp.com/todolist/</td>
 	<tr>
 		<td>Login</td>
 		<td>https://tugas2-pbp-febidamanik.herokuapp.com/todolist/login</td>
  <tr>
    <td>Registrasi Akun</td>
    <td>https://tugas2-pbp-febidamanik.herokuapp.com/todolist/register</td>
  <tr>
    <td>Pembuatan task</td>
 		<td>https://tugas2-pbp-febidamanik.herokuapp.com/todolist/create-task</td>
  <tr>
    <td>Logout</td>
 		<td>https://tugas2-pbp-febidamanik.herokuapp.com/todolist/logout</td>
   </tr>
 </table>

</body>
</html>

# 🔐Peran penting {% csrf_token %} pada elemen <form>🔐
Berbagai jenis serangan dapat terjadi di situs web salah satu serangan tersebut bernama Cross-Site Request Forgery yang sering disebut sebagai CSRF. Serangan ini dilakukan dengan menjalankan perintah yang seharusnya tidak diizinkan lewat berbagai aplikasi situs web atau lainnya sebagai medianya. Salah satu cara untuk mencegah serangan tersebut dengan menggunakan CSRF Token. CSRF Token adalah susunan acak berupa string dan unik yang dihasilkan setiap kali halaman formulir ditampilkan. Dengan CSRF Token, setiap form yang sudah disubmit akan disisipkan di dalam POST request sebagai header, atau form data, atau query string kemudian dari sisi backend dilakukan validasi apakah CSRF yang dikirim sepenuhnya valid atau tidak. Apabila tidak menggunakan csrf_token pada `<form>` maka penyerang dapat mengirim permintaan yang tidak diinginkan user sehingga fitur tersebut dapat dieksploitasi. 
	
# Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }}) ❓
Tentu saja hal tersebut dapat dilakukan. Django menyediakan berbagai cara untuk membuat elemen `<form>` tanpa harus menggunakan generator, seperti {{form.as_table}}). Bahkan, hanya dengan menggunakan fitur bawaan HTML form yang efektif dapat dibuat. 
	
# ⚒Gambaran besar cara membuat <form> secara manual⚒
Berikut gambaran besar cara membuat `<form>` secara manual, yaitu: 
- Dalam pembuatan secara manual, diawali dengan tag `<form>` dan diakhiri dengan `<form>`
- Kemudian ditambahkan dengan atribut `action` dan `method` agar dapat berfungsi sebagaimana mestinya. Action berupa alamat dari halaman PHP untuk mengirimkan data form sedangkan method berupa GET/POST untuk menjelaskan data isian form yang akan dikirim ke web browser
- Selanjutnya menambahkan tag <input> yang terdapat atribut `name="<nama-variable>"` sehingga diperoleh input berupa data dari user oleh `views.py` dengan memanggil perintah HTTP Request

# ◽Proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML◽

	
	
	
# 📌Pengimplementasian checklists dari tasks📌
