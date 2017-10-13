# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response

# Create your views here.

from django.http import HttpResponse


def index(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am a bold font from the context"}
    return render_to_response('books/index.html', context_dict, context)


def about(request):
    context = RequestContext(request)
    return render_to_response('books/about.html', {}, context)


def detail(request, book_id):
    return HttpResponse("<h2> Details of book ID " + str(book_id) + "</h2>")


def personal(request):
    return HttpResponse("<h1> This is my personal trial page </h1>")
