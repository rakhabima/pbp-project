from django.forms import ModelForm
from main.models import Book
from django import forms
from django.contrib.auth.models import User


class ProductForm(ModelForm):
    class Meta:
        model = Book
        fields = ["book_name", "author", "total_pages",
                  "date_published", "times_readed", "description", "user"]

    user = forms.ModelChoiceField(queryset=User.objects.all(), required=True)
