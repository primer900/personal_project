from django.shortcuts import render

# Create your views here.

from .models import Movie
from django.views import generic
from django.shortcuts import get_object_or_404, render

class IndexView(generic.ListView):
    model = Movie
    context_object_name = 'latest_movie_list'
    template_name = 'review/index.html'

class SynopsisView(generic.DetailView):
    model = Movie
    template_name = 'review/synopsis.html'
