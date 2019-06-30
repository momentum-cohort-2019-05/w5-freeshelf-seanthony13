from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User

class Catagory(models.Model):
    catagory = models.CharField(max_length=100)

    def __str__(self):
        return self.catagory

    def get_absolute_url(self):
        """Function that returns a link to access a unique detail record for a book catagory."""
        return reverse('catagory-detail', args=[str(self.id)])

# Create your models here.
class Book(models.Model):
    """Model Class representing a book (but not a specific copy of a book) in the database"""
    title = models.CharField(max_length=100)
    # Foreign Key used in author cuz (in this case) book can only have 1 author, but authors 
    # can have multiple books
    # Author as a string instead of object because it hasn't been declared yet in the file
    # Wouldn't be a string (in quotes) if I had an Author class
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    url = models.URLField(max_length=250)
    description = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    date_added = models.DateField(auto_now_add=True)
    

    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
    class Meta:
        ordering = ['-date_added']
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])

class Author(models.Model):
    """Model representing an author."""
    name = models.CharField(max_length=100, default ='anonymous')
    def __str__(self):
        return self.name

class UserFavs(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    fav_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ['owner', 'fav_book']
        ordering = ['-date_added']

    def __str__(self):
        return self.fav_book.title
