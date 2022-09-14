# 📑TUGAS-2 PBP📑
Nama  : Febi Claudia Damanik

NPM   : 2106751884

Kelas : D

Link aplikasi 🔗https://tugas2-pbp-febidamanik.herokuapp.com/katalog/

# Bagan Request Client dan Response ke Aplikasi Django 
![Bagan PBP](https://user-images.githubusercontent.com/112416751/190206240-52eed119-b548-4648-9bf1-e325ec75f591.jpg)

# Penjelasan Bagan
1. Setiap client yang mengakses Django akan dianggap sebagai bentuk permintaan oleh client sebelum masuk ke dalam Django
2. Kemudian permintaan client akan diproses lebih lanjut melalui urls.py
3. Pendefinisian alamat URL dan pendistribusian fungsi tiap route akan diatur di urls.py
4. Pada file urls.py, permintaan yang masuk dari client, seperti mengambil dan menyusun tampilan data pada templates akan diteruskan ke file views.py untuk terlebih dahulu diproses
5. Apabila saat pemrosesan diperlukan database, file views.py akan mengarahkan akses data dalam bentuk pemanggilan query ke models sehingga diperoleh data dari database
6. Setelah itu, database akan merespon pemanggilan query tersebut ke models yang akan dilanjutkan oleh file views.py untuk diimport
7. Hasil dari proses tersebut akan ditampilkan dalam format HTML di templates hingga akhirnya halaman HTML dikembalikan ke Django untuk ditampilkan kepada client sebagai bentuk respons

# 📌Mengapa kita menggunakan virtual environment?
Virtual Environment digunakan untuk memastikan bahwa versi library dari suatu project tidak akan berubah apabila terdapat update di library yang sama untuk project lainnya. Dengan menggunakan virtual environment, dapat membuat dependencies yang berbeda-beda antara satu project dengan lainnya tanpa mengubah configurations pada operating systems yang dipakai. Pada saat program Python berjalan di dalam virtualenv terdapat modul-modul sendiri yang membuat program dari luar tidak bisa mengaksesnya. Dengan begitu, pembuatan environment pada aplikasi web berbasis Django berguna sebagai tools untuk menyimpan modulnya masing-masing. Tidak hanya Django, penggunaan tools virtualenv umumnya disarankan untuk digunakan saat membuat aplikasi versi Python. Contohnya, pada saat kita ingin mengakses folder project yang berbeda apabila environment dari kedua project dan versi dari Django tersebut berbeda kita masih bisa dapat menjalankan aplikasi dengan berbagai macam versi agar memiliki struktur direktori mandiri.


# 📌Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Dalam pembuatan aplikasi web berbasis Django, program tetap dapat dijalankan tanpa virtual environment namun pengguna hanya dapat mengakses modul-modul global saja. Saat meng-install modul menggunakan ‘pip’, modul akan secara otomatis ter-install secara global di ‘/usr/lib/python2.7/site-packages’. Karena modul ter-install secara global semua aplikasi dapat mengakses dan menggunakannya dan sebenarnya hal ini tidak terlalu dipermasalahkan. Namun, hanya saja saat membuat proyek aplikasi menggunakan django versi lama dan kemudian modulnya di-upgrade membuat aplikasi yang sudah dibuat sebelumnya tidak dapat berjalan dengan modul yang sudah di-upgrade. Hal ini disebabkan modul yang sudah di-upgrade tersebut mengalami banyak perubahan fungsi dibandingkan modul sebelumnya.

# 📌Pengimplementasian Project
- Membuat fungsi show_katalog yang akan menerima parameter request untuk dikembalikan ke dalam fungsi render(request, "katalog.html", context) dari Django. 
- Pada function show_katalog(), disimpan semua objek dari CatalogItem yang terdapat pada sebuah variabel data_katalog_item dimana terdiri dari sebuah key dan value dari semua objek CatalogItem berupa list barang, nama, dan npm. Setelah itu, akan direturn function render() yang berisi parameter request, file html, html katalog, dan context.
- Pada file urls.py di folder katalog, ditambahkan urlpatterns untuk memetakan fungsi show_katalog. Selain itu, pada urls.py di project_django ditambahkan path dengan parameter 'katalog/' yang akan menuju ke katalog.urls sehingga dapat memetakan fungsi show_katalog.
- Pada file dengan format json akan diload data sehingga data dapat tersimpan di database lokal Django hingga semua data yang ada di dalam folder template pada file katalog.html pada database lokal dapat dimuat serta ditampilkan.
- Membuat aplikasi di Heroku serta membuat repositori git lokal dan daring (GitHub).
- Melakukan deployment dengan menyalin API Key dan menyimpan informasi tentang aplikasi Heroku dari akun pribadi API.
- Terakhir _re-running workflows and jobs_ pada tab Actions repository GitHub dan mengakses link tautan project aplikasi yang telah berhasil dideploy di Heroku untuk menjalankan aplikasinya.
