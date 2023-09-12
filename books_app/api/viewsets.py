from rest_framework import viewsets
from books_app.api import serializers
from books_app.models import Books

class BookViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = serializers.BookSerializer