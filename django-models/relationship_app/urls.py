from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth import views as auth_views
from . import views
from .views import admin_view, librarian_view, member_view, add_book_view, edit_book_view, delete_book_view

urlpatterns = [
    path('books/', list_books, name='book-list'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin-view/', admin_view, name='admin-view'),
    path('librarian-view/', librarian_view, name='librarian-view'),
    path('member-view/', member_view, name='member-view'),
    path('add_book/', add_book_view, name='add-book'),
    path('edit_book/<int:pk>/', edit_book_view, name='edit-book'), 
    path('books/delete/<int:pk>/', delete_book_view, name='delete-book'),
]