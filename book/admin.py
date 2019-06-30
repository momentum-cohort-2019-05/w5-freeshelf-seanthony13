from django.contrib import admin
from .models import Book, Author, Catagory
from book.models import Author, Book

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Catagory)
# admin.site.register(Genre)