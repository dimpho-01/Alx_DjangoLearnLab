## Python command

```python
from bookshelf.models import Book
deleted_book = Book.objects.get(title = 'Nineteen Eighty-Four')
deleted_book.delete()
books = Book.objects.all()
print(books)
```

## Expected Output

The Book instance is successfully deleted.
(1, {'bookshelf.Book': 1})
<QuerySet []>