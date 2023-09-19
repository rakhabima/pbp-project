#TUGAS 2

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

#TUGAS 3
1. Apa perbedaan antara form POST dan GET dalam Django?
   - form POST digunakan untuk melakukan sesuatu yang mengubah keadaan dalam server/aplikasi, sedangkan jika GET digunakan tidak akan mengubah sesuatu dalam server/aplikasi
2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
   - HTML merupakan singkatan dari HyperText Markup Language yang digunakan untuk menuliskan struktur dari sebuah web. HTML berbentuk tag-tag yang berisi tipe konten dan mengirimkan isi konten.
   - XML adalah singkatan dari eXtensible Markup Language. Tag-tag yang terdapat pada XML bisa menggunakan nama yang mendeskripsikan data yang terdapat di dalam tag tersebut.
   - JSON adalah singkatan dari JavaScript Object Notation format untuk pertukaran data yang ringan. Walaupun dalam namanya terdapat kata JavaScript tetapi format file json tidak bergantung terhadap bahasa pemrograman apapun, tetapi menggunakan bentuk objek dari JavaSript.
3.  Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
   - JSON lebih mudah untuk digunakan dalam menuliskan data yang berukuran kecil. JSON juga lebih efisien untuk digunakan dalam membuat API. Ukuran file JSON relatif lebih kecil dibandingkan dengan file XML.
4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   - membuat form untuk menginput data dengan membuat file `forms.py` dan membuat struktur form di file tersebut
   ```
   from django.forms import ModelForm
   from main.models import Book

   class ProductForm(ModelForm):
      class Meta:
         model = Book
         fields = ["book_name", "author", "total_pages", "date_published", "description"]
   ```

   - menambahkan beberapa import pada file `views.py` pada folder `main` lalu membuat fungsi baru dengan nama `create_product` seperti berikut
   ```
      def create_product(request):
         form = ProductForm(request.POST or None)

         if form.is_valid() and request.method == "POST":
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))

         context = {'form': form}
         return render(request, "create_product.html", context)
   ```

   - mengganti isi fungsi `show_main` menjadi seperti berikut
   ```
      def show_main(request):
      products = Book.objects.all()

      context = {
         'book_name': 'The Richest Man in Babylon',
         'author': 'George S. Clason',
         'total_pages': 144,
         'description': 'The Richest Man in Babylon is a 1926 book by George S. Clason that dispenses financial advice through a collection of parables set 4,097 years earlier, in ancient Babylon. The book remains in print almost a century after the parables were originally published, and is regarded as a classic of personal financial advice.',
         'products': products,
      }

      return render(request, "main.html", context)
   ```

   - menambah import fungsi `create_product` pada file `urls.py` di folder `main`
   ```
   from main.views import show_main, create_product
   ```

   -  menambahkan path url baru ke dalam `urlpatterns` di file `urls.py`

   - membuat file html baru bernama `create_product.html` di folder `main/templates` dan mengisinya dengan kode yang membuat form method post
   ```
   {% extends 'base.html' %} 

   {% block content %}
   <h1>Add New Product</h1>

   <form method="POST">
      {% csrf_token %}
      <table>
         {{ form.as_table }}
         <tr>
               <td></td>
               <td>
                  <input type="submit" value="Add Product"/>
               </td>
         </tr>
      </table>
   </form>

   {% endblock %}
   ```

   - menambah kode berikut ini ke main.html di dalam `{% block content %}`
   ```
   <table>
    <tr>
        <th>Name</th>
        <th>Author</th>
        <th>Total Pages</th>
        <th>Date Published</th>
        <th>Description</th>
        <th>Date Added</th>
    </tr>

    {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}

    {% for product in products %}
        <tr>
            <td>{{product.name}}</td>
            <td>{{product.author}}</td>
            <td>{{product.total_pages}}</td>
            <td>{{product.date_published}}</td>
            <td>{{product.description}}</td>
            <td>{{product.date_added}}</td>
        </tr>
    {% endfor %}
   </table>

   <br />

   <a href="{% url 'main:create_product' %}">
      <button>
         Add New Product
      </button>
   </a>
   ```

   - Menampilkan data dalam bentuk JSON dan XML dengan mengubah isi file  `views.py`
   - Menambahkan import `HttpResponse` dari `django.http` dan `serializers` dari `django.core`
   - Membuat fungsi baru dengan parameter request dengan nama `show_xml`, `show_json`, `show_xml_by_id` dan `show_json_by_id`. Lalu membuat variabel di dalam fungsi yang menyimpan query data pada Book. Lalu mereturn data di dalam variabel yang sudah dilakukan method `serialize`
   ```
   def show_xml(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
   ```

   ```
   def show_json(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
   ```

   ```
   def show_xml_by_id(request, id):
    data = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
   ```

   ```
   def show_json_by_id(request, id):
    data = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
   ```
   - Method show_xml_by_id dan show_json_by_id meng-query data pada book sesuai dengan id yang dimasukkan ke dalam parameter url

   - mengimpor fungsi yang sudah dibuat ke file `urls.py` pada folder `main`
   ```
   from main.views import show_main, create_product, show_xml, show_json, show_json_by_id, show_xml_by_id
   ```
   - menambahkan path url ke dalam `urlpatterns` sesuai dengan fungsi yang sudah dibuat
   ```
   path('xml', show_xml, name='show_xml'),
    path('json', show_json, name='show_json'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id')
   ```
   
### Screenshot response url dari postman
   - Main page di postman
   ![response main page from postman](./main/static/main-page.png)

   - Response JSON dari postman
   ![response main page from postman](./main/static/json.png)

   - Response JSON sesuai ID dari postman
   ![response main page from postman](./main/static/json-id.png)

   - Response XML dari postman
   ![response main page from postman](./main/static/xml.png)

   - Response XML sesuai ID dari postman
   ![response main page from postman](./main/static/xml-id.png)