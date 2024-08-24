from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import View
from .models import Book
from .forms import ExampleForm

# Create your views here.
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'bookshelf/book_list.html', context)


@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    # The logic to edit a book goes here
    pass

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a new URL or inform of successful creation
    else:
        form = ExampleForm()
    
    return render(request, 'bookshelf/form_example.html', {'form': form})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    # The logic to delete a book goes here
    pass

class EditBookView(PermissionRequiredMixin, View):
    permission_required = 'bookshelf.can_edit'
    # rest of the view logic