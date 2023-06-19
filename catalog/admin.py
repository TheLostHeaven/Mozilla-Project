from django.contrib import admin

# Register your models here.

from .models.book import Book
from .models.author import Author
from .models.book_instance import BookInstance
from .models.genre import Genre
from .models.languaje import Language

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)