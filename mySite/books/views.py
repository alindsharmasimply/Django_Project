# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
# Create your views here.
from .models import Book
from django.http import HttpResponse


def index(request):
    template = loader.get_template('books/index.html')
    all_books = Book.objects.all()
    context = {
        'all_books': all_books
    }
    return HttpResponse(template.render(context, request))


def about(request):
    template = loader.get_template('books/about.html')
    return HttpResponse(template.render(request))


def detail(request, book_id):
    return HttpResponse("<h2> Details of book ID " + str(book_id) + "</h2>")


def personal(request):
    return HttpResponse("<h1> This is my personal trial page </h1>")


def database_access(request):
    all_books = Book.objects.all()
    html = ''
    for book in all_books:
        url = '/books/' + str(book.id) + '/'
        html += '<a href = "' + url + '">' + str(book.name) + '</a></br>'
    return HttpResponse(html)
