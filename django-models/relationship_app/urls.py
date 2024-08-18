from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth import views as auth_views
from .views import SignUpView

urlpatterns = [
    path('books/', list_books, name='book-list'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', SignUpView.as_view(), name='register'),

]