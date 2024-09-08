from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from api.models import Author, Book
from rest_framework import status
from django.urls import reverse

class BookAPITestCase(APITestCase):
    
    def setUp(self):
        # Set up initial data and a test user.
        self.user = User.objects.create_user(username='testuser', password='password')
        self.author = Author.objects.create(name='Author Name')
        
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
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.data['author'], data['author'])
        self.assertEqual(response.data['publication_year'], data['publication_year'])
        self.assertEqual(Book.objects.count(), 1)