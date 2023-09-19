from django.db import models

class Book(models.Model):
    book_name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    date_published = models.DateField(max_length=255)
    total_pages = models.IntegerField()
    description = models.TextField()