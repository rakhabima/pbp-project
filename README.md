1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

   - Membuat direktori dengan nama reading-list. Nama bisa disesuaikan dengan nama project yang ingin dibuat.
   - Membuat virtual environment pada direktori tersebut.
   - Mendownload dependencies yang dibutuhkan dalam pembuatan project.
   - Membuat proyek Django dengan nama reading_list. Dengan menuliskan
     `   django-admin startproject reading_list .`
     pada terminal
   - Membuat aplikasi baru pada proyek dengan menjalankan `python manage.py startapp main` pada terminal
   - Mendaftarkan aplikasi yang sudah dibuat ke dalam proyek. Dengan cara memasukkan `main` pada variable `INSTALLED_APPS` yang terdapat pada file settings.py di direktori proyek.
   - Membuat direktori baru pada main dengan nama templates dan membuat file html di dalamnya.
   - Membuat kode html sesuai dengan yang diinginkan
   - Mengubah file `models.py` dan mengisinya dengan class model yang diinginkan

   ```
    from django.db import models

    class Book(models.Model):
        book_name = models.CharField(max_length=255)
        author = models.CharField(max_length=255)
        date_added = models.DateField(auto_now_add=True)
        total_pages = models.IntegerField()
        description = models.TextField()
   ```

   - melakukan migrasi agar data sesuai dengan model yang dibuat.
   - menghubungkan komponen view dan template dengan mengubah isi file `views.py` pada direktori `main`.
   - mengimpor render dari django.shortcuts

   ```
    from django.shortcuts import render
   ```

   - Menambahkan fungsi `show_main` dan isi objek `context` dengan data yang diinginkan

   ```
   def show_main(request):
    context = {
        context = {
        'book_name': 'The Richest Man in Babylon',
        'author': 'George S. Clason',
        'total_pages': 144,
        'description': 'The Richest Man in Babylon is a 1926 book by George S. Clason that dispenses financial advice through a collection of parables set 4,097 years earlier, in ancient Babylon. The book remains in print almost a century after the parables were originally published, and is regarded as a classic of personal financial advice.'
        }
    }

    return render(request, "main.html", context)
   ```

   - Mengonfigurasikan URL pada aplikasi `main`
   - Buat file `urls.py` pada `main` dan isi dengan kode berikut

   ```
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
   ```

   - Setelah itu mengonfigurasikan URL pada proyek dengan mengimpor fungsi include dari django.urls pada file `urls.py` di direktori proyek
   - Menambahkan URL agar menampilkan main pada variabel `urlpatterns`.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
   ![bagan request client ke web Django](./main/static/BAGAN-MVT.png)

   - Pada bagan tersebut terdapat client, url, model, dan juga template. Lalu apa kaitan antara file-file urls.py, views.py, models.py, dan berkas html?
   - File urls.py bertugas untuk routing url, atau dalam kata lain mengatur alur dari request dan response web agar melalui link sesuai dengan request client.
   - Lalu views.py merupakan file yang bertugas untuk mengatur dan mengolah data yang akan ditampilkan kepada client
   - Ada pula models.py yang merupakan file untuk sebagai penghubung antara proyek dan juga database.
   - dan terakhir ada berkas-berkas html yang merupakan file dalam web yang ditampilkan kepada client/user

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
   Virtual environment berfungsi untuk mengisolasi projek yang sedang dikerjakan dari system global, sehingga hal-hal yang dilakukan seperti mendownload dependencies tidak menggangu proyek python lainnya. Sebetulnya bisa saja membuat aplikasi web Django tanpa menggunakan virtual environment tetapi jika ada proyek django lainnya maka jika terdapat perubahan bisa saja proyek lain tersebut ikut terkena imbas dari perubahan tersebut.

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
   - MVC merupakan singkatan dari Model-View-Controller. Pada pola pemrograman ini kode dibagi menjadi 3 komponen yaitu model yang berfungsi untuk berkomunikasi dengan database dan mengatur logic dibalik layar dari program. Lalu ada view yang berisikan file-file yang akan dilihat oleh user, dan ada controller yang menghubungkan antara model dan juga view
   - MVT merupakan singkatan dari Model-View-Template. MVT ini memiliki beberapa kesamaan dengan MVC, namun pada MVT views bisa melakukan HTTP response dan request. Template pada MVT juga berisi file-file html yang akan ditampilkan kepada user.
   - MVVM adalah singkatan dari Model-View-ViewModel. Pada pemrograman ini model dan viewmodel bertugas untuk mengambil dan menyimpan data, dan view bertugas menampilkan data-data tersebut kepada user. Viewmodel juga berfungsi sebagai penghubung antara view dan model.
