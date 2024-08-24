from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import View

# Create your views here.
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    # Logic to edit a book
    pass

@permission_required('bookshelf.can_view', raise_exception=True)
def view_books(request):
    # Logic to view books
    pass

class EditBookView(PermissionRequiredMixin, View):
    permission_required = 'bookshelf.can_edit'
    # rest of the view logic