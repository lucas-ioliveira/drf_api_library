from rest_framework import serializers
from books_app.models import Books

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'