# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
# Create your views here.
from .models import Book
from django.http import HttpResponse
from django.http import Http404


def index(request):
    all_books = Book.objects.all()
    context = {
        'all_books': all_books
    }
    return render(request, 'books/index.html', context)


def about(request):
    template = loader.get_template('books/about.html')
    return HttpResponse(template.render({}, request))


def detail(request, book_id):
    try:
        book = Book.objects.get(id=book_id)

    except Book.DoesNotExist:
        raise Http404("OOoooPS !!! This book is not available")
    return render(request, 'books/detail.html', {'book': book})


def personal(request):
    return HttpResponse("<h1> This is my personal trial page </h1>")


def database_access(request):
    all_books = Book.objects.all()
    html = ''
    for book in all_books:
        url = '/books/' + str(book.id) + '/'
        html += '<a href = "' + url + '">' + str(book.name) + '</a></br>'
    return HttpResponse(html)
