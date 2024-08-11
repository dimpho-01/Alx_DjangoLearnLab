## Python command

```python
updated_book = Book.objects.get(title = '1984')
updated_book.title = 'Nineteen Eighty-Four'
updated_book.save()
```

## Expected Output

The title of the Book instance is successfully updated to 'Nineteen Eighty-Four'.