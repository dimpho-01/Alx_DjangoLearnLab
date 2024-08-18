from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth import login
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import UserProfile
from django.contrib.auth.decorators import permission_required
from .forms import BookForm
from django.http import HttpResponseRedirect
from django.contrib import messages

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
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(check_librarian_role)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(check_member_role)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a 'success' or 'book list' page
            return redirect('book-list')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book-list')  # Redirect to a 'book list' page
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        messages.success(request, "Book deleted successfully.")
        return HttpResponseRedirect(reverse('book-list'))  # Redirect to the book list
    return render(request, 'relationship_app/delete_book.html', {'book': book})