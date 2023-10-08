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

class BookDetailAPITest(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category", description="Test Description")
        self.book = Book.objects.create(
            title='Exploring the Galazy',
            author='Clayton Siby',
            description='The wonders of our Galaxy and beyond.',
        )

        self.updated_book_data = {
            'title': 'Steve Jobs',
            'author': 'Walter Isaacson',
            'description': 'Steve Jobs, the man who changed everything',
        }

        self.book.categories.set([self.category])
        self.url = reverse('book-detail', args=[self.book.id])
    
    def test_retrieve_book(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['book']['id'], str(self.book.id))
        self.assertEqual(response.data['book']['title'], self.book.title)
        self.assertEqual(response.data['book']['author'], self.book.author)
        self.assertEqual(response.data['book']['description'], self.book.description)
        self.assertEqual(response.data['book']['categories'], [self.book.categories.last().id])

    def test_update_book(self):
        self.updated_book_data['categories'] = [self.category.id]
        response = self.client.put(self.url, data=self.updated_book_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['message'], 'Success')
        self.assertEqual(response.data['book']['title'], self.updated_book_data['title'])
        self.assertEqual(response.data['book']['author'], self.updated_book_data['author'])
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, self.updated_book_data['title'])
        self.assertEqual(self.book.author, self.updated_book_data['author'])
        
    def test_delete_book(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())
