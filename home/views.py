""" Import render """

from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def about(request):
    """ A view to the about page """

    return render(request, 'home/about.html')


def grounding(request):
    """ A view about grounding """

    return render(request, 'home/grounding.html')
