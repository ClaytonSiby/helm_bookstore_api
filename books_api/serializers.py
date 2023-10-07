from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['pk', 'title', 'author', 'description', 'created_at', 'updated_at']
        read_only_fields = ['pk']
