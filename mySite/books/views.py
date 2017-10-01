# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>This is the books homepage</h1>")


def detail(request, book_id):
    return HttpResponse("<h2> Details of book ID " + str(book_id) + "</h2>")
