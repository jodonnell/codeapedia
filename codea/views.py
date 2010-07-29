from django import http
from django.shortcuts import render_to_response
from codea.models import Author, Book, Tags, Quotes

def index(request):
    authors = Author.objects.all()
    books = Book.objects.all()
    tags = Tags.objects.all()
    return render_to_response('index.html', {'authors':authors, 'books':books, 'tags':tags})

def by_book(request):
    id = int(request.GET['id'])
    quotes = Quotes.objects.filter(book=id)
    return render_to_response('quotes.html', {'quotes':quotes})

def by_author(request):
    id = int(request.GET['id'])
    quotes = Quotes.objects.filter(author=id)
    return render_to_response('quotes.html', {'quotes':quotes})

def by_tag(request):
    id = int(request.GET['id'])
    quotes = Quotes.objects.filter(tags=id)
    return render_to_response('quotes.html', {'quotes':quotes})
