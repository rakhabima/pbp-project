from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    book_name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    date_published = models.DateField(max_length=255)
    total_pages = models.IntegerField()
    # times_readed = models.IntegerField()
    description = models.TextField()