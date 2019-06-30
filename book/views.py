import csv
from django.shortcuts import render
from django.contrib import messages
from django. contrib.auth.decorators import permission_required
from .models import Book

# Create your views here.

def index(request):
    book_list = Book.objects.all()

    context = {'book-list': book_list }

    
    return render(request, 'index.html', context=context)