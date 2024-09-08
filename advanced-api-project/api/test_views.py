from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from api.models import Author, Book
from api.serializers import BookSerializer

class BookAPITestCase(APITestCase):
    
    def setUp(self):
        # Set up initial data and test user.
        self.user = User.objects.create_user(username='testuser', password='password')
        self.author = Author.objects.create(name='Author Name')
        self.book = Book.objects.create(
            title="Test Book",
            publication_year=2020,
            author=self.author
        )

    def test_create_book(self):
        self.client.login(username='testuser', password='password')
        url = reverse('book-create')
        data = {
            'title': "Another Test Book",
            'publication_year': 2021,
            'author': self.author.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.latest('id').title, data['title'])
