from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth import login
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import UserProfile

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('post-login')) 
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

def check_admin_role(user):
    return user.is_authenticated and UserProfile.objects.get(user=user).role == 'Admin'

def check_librarian_role(user):
    return user.is_authenticated and UserProfile.objects.get(user=user).role == 'Librarian'

def check_member_role(user):
    return user.is_authenticated and UserProfile.objects.get(user=user).role == 'Member'

@login_required
@user_passes_test(check_admin_role)
def admin_view(request):
    return HttpResponse("Admin View")

@login_required
@user_passes_test(check_librarian_role)
def librarian_view(request):
    return HttpResponse("Librarian View")

@login_required
@user_passes_test(check_member_role)
def member_view(request):
    return HttpResponse("Member View")