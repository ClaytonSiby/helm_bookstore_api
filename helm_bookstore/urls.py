"""
URL configuration for helm_bookstore project.
"""

from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from books_api import views

urlpatterns = format_suffix_patterns([
    path('api/admin/', admin.site.urls),
    path('api/books/', views.get_books_list, name='books'),
    path('api/books/add_book/', views.create_book, name="add_book"),
    path('api/books/<int:pk>/', views.get_book_details, name="book_details"),
    path('api/books/<int:pk>/update/', views.update_book, name="update_book"),
    path('api/books/<int:pk>/delete/', views.delete_book, name="delete_book"),
])
