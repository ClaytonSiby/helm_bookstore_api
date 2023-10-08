from django.urls import reverse
from rest_framework.test import APITestCase
from books_api.models import Book, Category
from books_api.serializers import BookSerializer, CategorySerializer

class BookListCreateAPITest(APITestCase):
    def setUp(self):
        self.url = reverse('book-list-create')
        self.book_data = {'title': 'As a man Thinketh', 'author': 'James Allen', 'description': 'Thought and Circumstances'}
        
    def test_list_books(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['message'], 'Success')
        self.assertEqual(len(response.data['books']), Book.objects.count())
        
    def test_create_book(self):
        category = Category.objects.create(name="Self Help", description="Books about self help")
        self.book_data['categories'] = [category.id]
        response = self.client.post(self.url, data=self.book_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['message'], 'Success')
        self.assertEqual(response.data['book']['title'], self.book_data['title'])
        self.assertEqual(response.data['book']['author'], self.book_data['author'])
        self.assertEqual(response.data['book']['description'], self.book_data['description'])
        self.assertEqual(Book.objects.count(), 1)
