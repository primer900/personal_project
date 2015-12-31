from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Movie
# Create your views here.

def index(request):
    latest_movie_list = Movie.objects.order_by('-rating')[:5]
    template = loader.get_template('movie/index.html')
    context = {
        'latest_movie_list': latest_movie_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, movie_id):
    response = "You're looking at movie %s."
    return HttpResponse(response % movie_id)

def review(request, movie_id):
    response = "You're looking at the review of movie %s."
    return HttpResponse(response % movie_id)
