from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def toPage(request, a):
    a = a + '.html'
    return render(request, a)


def blogPage(request):
    return render(request, 'blog.html')
