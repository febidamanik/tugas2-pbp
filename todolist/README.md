# 📑TUGAS-4 PBP📑

**Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django**

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
 		<td>📟Halaman Utama</td>
 		<td>https://tugas2-pbp-febidamanik.herokuapp.com/todolist/</td>
 	<tr>
 		<td>🟢Login</td>
 		<td>https://tugas2-pbp-febidamanik.herokuapp.com/todolist/login</td>
  <tr>
    <td>🙎‍Registrasi Akun</td>
    <td>https://tugas2-pbp-febidamanik.herokuapp.com/todolist/register</td>
  <tr>
    <td>📩Pembuatan task</td>
 		<td>https://tugas2-pbp-febidamanik.herokuapp.com/todolist/create-task</td>
  <tr>
    <td>🔴Logout</td>
 		<td>https://tugas2-pbp-febidamanik.herokuapp.com/todolist/logout</td>
   </tr>
 </table>

</body>
</html>

# 🔐Peran penting {% csrf_token %} pada elemen form🔐
Berbagai jenis serangan dapat terjadi di situs web salah satu serangan tersebut bernama Cross-Site Request Forgery yang sering disebut sebagai CSRF. Serangan ini dilakukan dengan menjalankan perintah yang seharusnya tidak diizinkan lewat berbagai aplikasi situs web atau lainnya sebagai medianya. Salah satu cara untuk mencegah serangan tersebut dengan menggunakan CSRF Token. CSRF Token adalah susunan acak berupa string dan unik yang dihasilkan setiap kali halaman formulir ditampilkan. Dengan CSRF Token, setiap form yang sudah disubmit akan disisipkan di dalam POST request sebagai header, atau form data, atau query string kemudian dari sisi backend dilakukan validasi apakah CSRF yang dikirim sepenuhnya valid atau tidak. Apabila tidak menggunakan csrf_token pada `<form>` maka penyerang dapat mengirim permintaan yang tidak diinginkan user sehingga fitur tersebut dapat dieksploitasi. 
	
# Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }}) ❓
Tentu bisa, pembuatan form dapat dilakukan secara manual. Django menyediakan berbagai cara untuk membuat elemen `<form>` tanpa harus menggunakan generator, seperti {{form.as_table}}). Bahkan, hanya dengan menggunakan fitur bawaan HTML form yang efektif dapat dibuat. 
	
# ⚒Gambaran besar cara membuat <form> secara manual⚒
Berikut gambaran besar cara membuat `<form>` secara manual, yaitu: 
- Dalam pembuatan secara manual, diawali dengan tag `<form>` dan diakhiri dengan `<form>`
- Kemudian ditambahkan dengan atribut `action` dan `method` agar dapat berfungsi sebagaimana mestinya. Action berupa alamat dari halaman PHP untuk mengirimkan data form sedangkan method berupa GET/POST untuk menjelaskan data isian form yang akan dikirim ke web browser
- Selanjutnya menambahkan tag <input> yang terdapat atribut `name="<nama-variable>"` sehingga diperoleh input berupa data dari user oleh views.py dengan memanggil perintah HTTP Request

# 🔽Proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML🔽
- User memberikan input pada form HTML yang berdasarkan isian yang diminta oleh form.
- Pada views.py terdapat fungsi yang akan menerima input user di HTML.
- Dengan menggunakan perintah `request.POST.get("<name>")` , data inpu akan disimpan ke dalam suatu variabel.
- Dibuat object Task baru yang akan menyimpan variabel judul dan deskripsi kemudian disimpan ke dalam database kemudian dengan menggunakan perintah <object>.save().
- Dengan menggunakan perintah `tasks = Task.objects.filter(user_id=user_id)` pada fungsi main, yaitu show_todolist akan didapatkan objek yang merupakan bagian dari objek Task sesuai dengan kepemilikan masing-masing user.
- Untuk menampilkan objek Task secara keseluruhan pada template HTML maka dijalankan dengan menggunakan perintah render.
- Dilakukan iterasi pada todolist untuk menampilkan satu kesatuan tabel pada template HTML yang formatnya disesuaikan dengan format pengaturan HTML.
	
# 📌Pengimplementasian checklists dari tasks📌
- Membuat django-app dengan 'startnewapp' diberi nama todolist dengan command berikut.
```
python manage.py startapp todolist
```
- Menambahkan path aplikasi todolist ke dalam 'urls.py' di project_django.
```
urlpatterns = [
    ...
    path('todolist/', include('todolist.urls')),
]
```
- Membuat task class serta atribut data `user`, `date`, `title`, `description`, dan `is_finished` 
```
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField() 
    title = models.CharField(max_length=150)
    description = models.TextField()
    is_finished = models.BooleanField(default=False)
```
- Membuat form registrasi dalam views.py di todolist.
``` 
form = UserCreationForm()
```
- Membuat fungsi berupa form login dan logout dengan method POST
```
    if request.method == "POST":
        form = UserCreationForm(request.POST)
```
- Membuat form pembuatan task baru pada main function dalam show_todolist dengan mengimplementasikan fungsi create_task.
```
def create_task(request):
    if request.method == "POST":
        judul = request.POST.get("judul")
        deskripsi = request.POST.get("deskripsi")
        newTask = Task(user=request.user, title=judul, description=deskripsi, date=datetime.now())
        newTask.save()
        return redirect("todolist:show_todolist")
    return render(request, "create_task.html")
```
- Membuat routing terhadap fungsi views.py dalam urls.py di todolist sehingga halaman HTML dapat ditampilkan lewat browser.
```
from django.urls import path
from todolist.views import delete_task, show_todolist, registrasi_user, login_user, logout_user, create_task, delete_task, update_task

app_name = "todolist"

urlpatterns = [
    path('', show_todolist, name="show_todolist"),
    path('register/', registrasi_user, name="registrasi_user"),
    path('login/', login_user, name="login_user"),
    path('logout/', logout_user, name="logout_user"),
    path('create-task/', create_task, name="create_task"), 
    path('delete/<int:id>', delete_task, name="delete_task"),
    path('update/<int:id>', update_task, name="update_task"),
]
```
- Melakukan deployment aplikasi Django pada Heroku menggunakan repository yang sama dari GitHub dengan Tugas 2 untuk memberikan perubahan pada repository sehingga nantinya dapat diakses melalui Internet jika sudah berhasil kita dapat mengakses link proyek aplikasi.
plus
```	
	git add .
	git commit -m "some commit message"
	git push origin <the branch name>
```	
**◻Tambahan Implementasi Bonus◻**
- Membuat dua akun pengguna beserta tiga dummy data menggunakan model Task di situs web dimana terdapat tambahan kolom untuk tombol yang akan melakukan behavior yang diinginkan, yaitu mengubah status serta tambahan kolom untuk menghapus suatu task.
![image](https://user-images.githubusercontent.com/112416751/192825790-658c8b5b-7cce-4d2f-82be-b2a06fff59c7.png)
![image](https://user-images.githubusercontent.com/112416751/192826306-86681ba8-99e4-4850-81fa-5b4065087915.png)

- Memperbarui status penyelesaian task dan tombol pengubahan status pada todolist.html
```
<a href="/todolist/update/{{task.id}}">
	<button class="button2" type="submit">Perbarui Status🔄</button>
</a>
```
- Menghapus suatu task todolist.html
```
<a href="/todolist/delete/{{task.id}}">
	<button class="button2" type="submit">Hapus❌</button>
</a>
```
=========================================================================================

# 📑TUGAS-5 PBP📑

**Tugas 5: Web Design Using HTML, CSS, and CSS Framework**

# 📊Inline, Internal, dan External CSS📊
Terdapat 3 (tiga)  cara untuk menambahkan CSS ke dalam file HTML dari website. 
- **1️⃣ Inline CSS (inline tag of HTML)**

Dengan penggunaan Inline CSS, kita menambahkan atribut `style` ke tag HTML tertentu dimana akan mengubah satu elemen saja. 
Contoh : 
	```html
	 <h1 style="color:white;padding:10px;">Tugas-5 PBP</h1>
	```
- **2️⃣ Internal CSS (inside HTML)**

Dengan penggunaan Internal CSS, kita akan menambahkan deklarasi kode CSS ke dalam tag `<style>`, di dalam `head` HTML. Dapat menggunakan ID, class, atau elemen untuk merujuk pada kode CSS.
Contoh :
	```html
	<head>
	<style>
	p{
        font-family: 'Acme';
        font-size:small;
        line-height: 12%;
	</style>
	</head>
	```
	Pengaplikasian pada tag HTML

	```html
	<body>
	<p>Mengerjakan tugas-5 pbp itu menyenangkan</p>
	</body>
	```
- **3️⃣ External style sheet (separated file)**

Dengan penggunaan External CSS, kita akan menambahkan kode pada file berekstensi .css terpisah dari HTML. Pada setiap laman HTML, harus menyertakan referensi ke file css tersebut di dalam tag `<link rel>`, di dalam `<head>` serta mengalokasikan file css pada folder yang sama dengan HTML. 
Contoh	: 
```html
<head>
  <link rel="stylesheet" type="text/css" href="style.css" />
</head>
```

# ⚖Kelebihan dan kekurangan dari setiap style⚖
Berikut penjelasan serta kelebihan dan kekurangan dari ketiga style tersebut, yaitu :
- **1️⃣ Inline CSS (inline tag of HTML)**

🔆Kelebihan🔆	:

	- Mudah melakukan modifikasi atau perbaikan
	- Memiliki proses permintaan HTTP yang relatif kecil
	- Tidak perlu membuat file CSS terpisah karena dapat secara langsung ditambahkan ke tag HTML

♨Kekurangan♨ 	:

	- Kurang efisien karena harus diimplementasikan pada setiap elemen
	- Kurang terstruktur apabila menggunakan banyak styling pada file HTML
	
- **2️⃣ Internal CSS (inside HTML)**

🔆Kelebihan🔆	:

	- Mudah untuk mengatur laman web dengan tampilan yang unik
	- Tidak perlu membuat file CSS terpisah karena dapat secara langsung oleh tag `<head>` `</head>` dan diawali dengan tag `<style>`

♨Kekurangan♨ 	:

	- Kurang efisien karena apabila menggunakan CSS yang sama harus mendeklarasikan tag dalam beberapa file
	- Kurang efektif karena memerlukan loading time yang cukup lama pada website

- **3️⃣ External style sheet (separated file)**

🔆Kelebihan🔆	:

	- Kode HTML lebih terstruktur dan rapi
	- Lebih efisien karena file css dapat digunakan berulang untuk laman website yang berbeda
♨Kekurangan♨ 	:

	- Memerlukan loading time tertentu untuk mengakses styling yang digunakan file dari CSS saat menampilkan laman website
	
# 🔖Tag pada HTML5🔖
◽ `<main>` `</main>` → Menyajikan bagian konten utama dari halaman
	
◽ `<header>` `</header>` → Menyajikan bagian header dari halaman sebagai konten pengantar
	
◽ `<dialog>` `<dialog>` → Menyajikan kotak dialog
	
◽ `<canvas>` `</canvas>` → Menyisipkan area untuk grafik, image, dan teks
	
◽ `<nav>` `</nav>` → Menyajikan link menu navigasi
	
◽ `<aside>` `</aside>` → Menyajikan konten pelengkap pada artikel utama
	
◽ `<section>` `</section>` → Menyajikan suatu bagian dokumen/aplikasi
	
◽ `<article>` `</article>` → Menyajikan konten yang bersifat _stand alone_
	
◽ `<footer>` `</footer>` → Menyajikan bagian footer pada halaman
	
◽ `<menuitem>` `</menuitem>` → Mendefinisikan list command yang dapat dipilih pengguna

# ⚜Tipe-tipe CSS Selector⚜
Berdasarkan urutan prioritasnya CSS Selector dibedakan menjadi :
	
1. ID Selectors, menggunakan ID pada tag selector-nya diawali dengan tanda pagar `#` atau hash.  
```html
	#header {
font-color: white
font-size: 14px;
font-weight: bold;
}
```html
2. Classes Selectors, menggunakan class pada tag sebagai selector-nya dibuat dengan tanda titik `.` di depannya.
```
	.button {
border: 0px;
background-color: #778cc0;
padding: 10px;
}
```html
3. Element Selector, menggunakan HTML pada tag sebagai selector-nya untuk mengubah atau memodifikasi style yang berada dalam tag tersebut.
```html
    td{
padding-left: 8px;
font-family: Tahoma, sans-serif;
font-size: 15px;
    }
```
	
# 📌Pengimplementasian checklists dari tasks📌
◽ ☑ Kustomisasi template untuk halaman login, register, dan create-task semenarik mungkin
Pada tugas-5, saya melakukan kustomisasi template dengan menggunakan Internal CSS (inside HTML).
Berikut langkah-langkah dalam pengimplementasian checklist di atas :
- Menambahkan deklarasi kode CSS ke dalam tag `<style>`, di dalam `head` HTML di tiap file HTML login, registration, todolist, create_task pada folder templates.
- Pada setiap file saya menginisialisasi class dan element styling untuk memperindah tampilan laman website, contohnya pada menu login berupa elemen tr, td, dan sebagainya.
- Dalam kustomisasi ini, saya juga melakukan import font yang tersedia di Google Fonts dengan menginisialisasi URL pada file HTML todolist
```html
    <head>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css?family=Secular One" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css?family=Alkalami" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css?family=Acme" rel="stylesheet">
    </head>
```
- Langkah terakhir, membuat keempat halaman yang dikustomisasi menjadi _responsive_. Dengan emasukkan tag meta viewport pada bagian head dari file HTML maka tag ini akan menginstruksikan browser untuk mengontrol dimensi serta skala pada laman website.
- Dengan menambahkan `content="width=device-width` maka lebar laman website akan disesuaikan dengan perangkat yang digunakan oleh pengguna sehingga konten sesuai yang ditampilkan sesuai dengan ukuran layar.
- Memberikan instruksi pada browser untuk mempertahankan ukuran CSS _pixels_ dan _device-independent pixels_ dengan ratio 1:1. 
Referensi dalam pengimplementasian Responsive Design : https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design#the_viewport_meta_tag
	
Pada folder templates tepatnya di file base.html untuk Tugas-2 PBP sudah tersedia tag meta viewport yang dimana pada aplikasi todolist pada tiap file-nya sudah terdapat `{% extends 'base.html' %}`. Untuk itu, sebagai tambahan dalam mengatur tampilan ukuran konten pada viewport saya menambahkan class selector, yaitu `.items {}`.

◽ ☑ Kustomisasi halaman utama _todo list_ menggunakan _cards_.
Berikut langkah-langkah dalam pengimplementasian checklist di atas :
- Pada file HTML todolist saya membuat class `.card` 
```html
    .card {
        margin:10px auto;
        padding:12px 60px;
        background-color:rgb(233, 243, 248);
        border-radius: 10px;
        box-shadow: 6px 2px 30px 0px rgba(0,0,0,0.75);
        backdrop-filter: blur(6px);
    }
```
Dengan penambahan class card, maka setiap penambahan task satu card akan mengandung satu task begitu pula seterusnya dengan memanfaatkan looping pada task di HTML.
```html
            {% for task in todolist %}
            <div class="card">
                <h4><b>┃{{task.title}}┃</b></h4>
                <p>📅{{task.date}}</p>
                <p>✍Description ➜ {{task.description}}</p>
                {% if task.is_finished == False %}
                <p>➖NOT COMPLETED➖</p> 
                {% else %} 
                <p>➖COMPLETED➖</p>
                {% endif %} 
```
**◻Tambahan Implementasi Bonus◻**
◽ ☑ Menambahkan efek ketika melakukan hover pada cards di halaman utama todolist	
- Dengan penambahan class untuk hover pada kode CSS dengan menambahkan insisialisasi `:hover`.
```html
    }
    .card:hover {
        box-shadow: 6px 2px 20px 0px #aebbdd;
        background-color: rgb(232, 236, 251);
    }		   	    
```		  
