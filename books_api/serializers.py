import uuid
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book, Category

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'description', 'created_at', 'updated_at', 'categories']
        extra_kwargs = {'id': {'read_only': True, 'default': serializers.CreateOnlyDefault(uuid.uuid4)}}


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'books']
        extra_kwargs = {'id': {'read_only': True, 'default': serializers.CreateOnlyDefault(uuid.uuid4)}}

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'books', 'created_at', 'updated_at']
        extra_kwargs = {'id': {'read_only': True, 'default': serializers.CreateOnlyDefault(uuid.uuid4)}}
