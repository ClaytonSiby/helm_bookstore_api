from django.contrib import admin
from django.urls import path, include
from books_api.views import (
    BookListCreateAPI,
    BookDetailAPI,
    CategoryListCreateAPI,
    CategoryDetailAPI,
)

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/accounts/', include('accounts.urls'), name='accounts'),
    path('api/books/', BookListCreateAPI.as_view(), name='book-list-create'),
    path('api/books/<uuid:pk>/', BookDetailAPI.as_view(), name='book-detail'),
    path('api/categories/', CategoryListCreateAPI.as_view(), name='category-list-create'),
    path('api/categories/<uuid:pk>/', CategoryDetailAPI.as_view(), name='category-detail'),
]
