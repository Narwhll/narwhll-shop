Davin Fauzan Akmalianto 2406409504 
Link = https://davin-fauzan-narwhllshop.pbp.cs.ui.ac.id/




2. ![alt text](image.png) 
    image dari scele: [text](https://scele.cs.ui.ac.id/pluginfile.php/269605/mod_resource/content/1/03%20-%20MTV%20Django%20Architecture.pdf)
    urls.py menerima request dari client, kemudian meneruskan request tersebut kepada views.py. Tugas views.py disini adalah mereturn main.html dengan informasi/konteks yang tersedia pada views.py. Contohnya disini, main.html menampilkan npm yang disediakan dari views.py. Models.py berfungsi sebagai definisi dari data yang akan kita pakai dalam aplikasi (seperti class).
 
3. file settings.py digunakan untuk membuat beberapa aturan yang diperlukan agar aplikasi berjalan dengan baik. contohnya seperti membuat list allowed_hosts, dimana itu berfungsi sebagai pengatur siapa saja yang boleh menghost aplikasi kita.

4. migrasi database dilakukan dengan cara menyimpan file models.py pada aplikasi, lalu menjalankan command python manage.py makemigrations, command ini akan menyiapkan untuk melakukan migrate (seperti ancang ancang), kemudian jalankan command python manage.py migrate untuk mengaplikasikan model kedalam database.

5. menurut saya, framework django dijadikan permulaan belajar karena sangat praktis untuk digunakan, dan ramah untuk pemula. Semua yang dibutuhkan pemula juga sudah ada di package django.

6. tidak