# Create

## Python command

```python
from bookshelf.models import Book
new_book = Book(title = '1984', author = 'George Orwell', publication_year = 1949)
new_book.save()
```

## Expected Output

The new Book instance is successfully created.

# Retrieve

## Python command

```python
retrieved_book = Book.objects.get(title="1984")
print(retrieved_book.title, retrieved_book.author, retrieved_book.publication_year)
```

## Expected Output

1984 George Orwell 1949

# Update

## Python command

```python
updated_book = Book.objects.get(title = '1984')
updated_book.title = 'Nineteen Eighty-Four'
updated_book.save()
```

## Expected Output

The title of the Book instance is successfully updated to 'Nineteen Eighty-Four'.

# Delete

## Python command

```python
deleted_book = Book.objects.get(title = 'Nineteen Eighty-Four')
deleted_book.delete()
books = Book.objects.all()
print(books)
```

## Expected Output

The Book instance is successfully deleted.
(1, {'bookshelf.Book': 1})
<QuerySet []>


