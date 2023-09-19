from django.forms import ModelForm
from main.models import Book

class ProductForm(ModelForm):
    class Meta:
        model = Book
        fields = ["book_name", "author", "total_pages", "date_published", "description"]