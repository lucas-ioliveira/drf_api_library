from django.db import models
from uuid import uuid4

class Books(models.Model):
    id_books = models.UUIDField(primary_key=True, default=uuid4, editable=False, verbose_name="Id Books")
    title = models.CharField(max_length=255, verbose_name="Title")
    author = models.CharField(max_length=255, verbose_name="Author")
    realease_year = models.IntegerField(verbose_name="Release Year")
    state = models.CharField(max_length=255, verbose_name="State")
    pages = models.IntegerField(verbose_name="Pages")
    publishing_company = models.CharField(max_length=255, verbose_name="Publishing Company")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

