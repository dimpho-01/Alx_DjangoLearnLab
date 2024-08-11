## Python command

```python
from bookshelf.models import Book
new_book = Book(title = '1984', author = 'George Orwell', publication_year = 1949)
new_book.save()
```

## Expected Output

The new Book instance is successfully created.