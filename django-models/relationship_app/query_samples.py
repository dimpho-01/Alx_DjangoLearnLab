from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_id):
    books = Book.objects.filter(author_id=author_id)
    for book in books:
        print(book.title)

def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    for book in books:
        print(book.title)

def retrieve_librarian_for_library(library_id):
    # Retrieve the librarian for a given library using `library_id`
    librarian = Librarian.objects.get(library_id=library_id)
    print(librarian.name)