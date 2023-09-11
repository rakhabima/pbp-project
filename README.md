1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   - Membuat direktori dengan nama reading-list. Nama bisa disesuaikan dengan nama project yang ingin dibuat.
   - Membuat virtual environment pada direktori tersebut.
   - Mendownload dependencies yang dibutuhkan dalam pembuatan project.
   - Membuat proyek Django dengan nama reading_list. Dengan menuliskan
     `    django-admin startproject reading_list .
   `
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
   