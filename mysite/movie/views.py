from django.shortcuts import render
from django.http import HttpResponse, Http404
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

def review(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist:
        raise Http404("This movie does not exist")
    return render(request, 'movie/review.html', {'movie': movie})

# def review(request, movie_id):
#    response = "You're looking at the review of movie %s."
#    return HttpResponse(response % movie_id)
