Davin Fauzan Akmalianto 2406409504 
Link = https://davin-fauzan-narwhllshop.pbp.cs.ui.ac.id/

1. 
 - "Membuat sebuah proyek Django baru." = membuat virtual environment dalam folder narwhll-shop, kemudian menginstall requirements yang diperlukan untuk memulai sebuah project django melalui sebuah .txt, kemudian menjalankan proyek dengan command yang disediakan django. setelah itu, membuat file .env serta .env.prod untuk membuat pengaturan environment untuk sesi production dan sesi non production.
 - "Membuat aplikasi dengan nama main pada proyek tersebut." =  menjalankan command 'python manage.py runserver main'.
 - "Melakukan routing pada proyek agar dapat menjalankan aplikasi main." = menyantumkan path('', include('main.urls')) dalam urlpatterns di file urls.py pada folder narwhll_shop, agar mengroute path default untuk menampilkan urls yang ada di folder main.
 - "Membuat model pada aplikasi main dengan nama Product beserta atribut atribut wajib." = mengedit file models.py yang berada di folder main, kemudian membuat atribut atribut dengan tipe datanya masing-masing sesuai arahan tugas.
 - "Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu." = pada views.py, buat fungsi untuk mencantumkan konteks/data yang diperlukan untuk menampilkan main.html, contoh menyantumkan value npm agar di main.html dapat ditampilkan valuenya, kemudian render main.html
 - "Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py." = pada urls.py yang terdapat di folder aplikasi main, import file views.py lalu jadikan path '' (path default) sebagai path yang mereturn fungsi show_main.  
 - "Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet." = mengikuti rangkaian pembuatan proyek di pws, kemudian mencantumkan link kedalam list ALLOWED_HOST pada file settings.py agar web dapat menjadi host aplikasi. 

2. ![alt text](image.png) 
    
    image dari scele: [Link SCELE](https://scele.cs.ui.ac.id/pluginfile.php/269605/mod_resource/content/1/03%20-%20MTV%20Django%20Architecture.pdf)
    urls.py menerima request dari client, kemudian meneruskan request tersebut kepada views.py. Tugas views.py disini adalah mereturn main.html dengan informasi/konteks yang tersedia pada views.py. Contohnya disini, main.html menampilkan npm yang disediakan dari views.py. Models.py berfungsi sebagai definisi dari data yang akan kita pakai dalam aplikasi (seperti class).
 
3. file settings.py digunakan untuk membuat beberapa aturan yang diperlukan agar aplikasi berjalan dengan baik. contohnya seperti membuat list allowed_hosts, dimana itu berfungsi sebagai pengatur siapa saja yang boleh menghost aplikasi kita.

4. migrasi database dilakukan dengan cara menyimpan file models.py pada aplikasi, lalu menjalankan command python manage.py makemigrations, command ini akan menyiapkan untuk melakukan migrate (seperti ancang ancang), kemudian jalankan command python manage.py migrate untuk mengaplikasikan model kedalam database.

5. menurut saya, framework django dijadikan permulaan belajar karena sangat praktis untuk digunakan, dan ramah untuk pemula. Semua yang dibutuhkan pemula juga sudah ada di package django.

6. tidak