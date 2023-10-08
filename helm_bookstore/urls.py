from django.contrib import admin
from django.urls import path
from books_api.views import (
    BookListCreateAPI,
    BookDetailAPI,
    CategoryListCreateAPI,
    CategoryDetailAPI,
)

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/books/', BookListCreateAPI.as_view(), name='book-list-create'),
    path('api/books/<int:pk>/', BookDetailAPI.as_view(), name='book-detail'),
    path('api/categories/', CategoryListCreateAPI.as_view(), name='category-list-create'),
    path('api/categories/<int:pk>/', CategoryDetailAPI.as_view(), name='category-detail'),
]
