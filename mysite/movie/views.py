from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Movie
from django.views import generic
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'movie/index.html'
    context_object_name = 'latest_movie_list'
    queryset = Movie.objects.all()

    # template = loader.get_template('movie/index.html')
    # context = {
    #     'latest_movie_list': latest_movie_list,
    # }
    # return HttpResponse(template.render(context, request))


class Review(generic.DetailView):
    model = Movie
    # queryset = Movie.objects.order_by('-rating')
    # context_object_name = 'latest_movie_list'
    template_name = 'movie/review.html'
    # try:
    #     movie = Movie.objects.get(pk=movie_id)
    # except Movie.DoesNotExist:
    #     raise Http404("This movie does not exist")
    # return render(request, 'movie/review.html', {'movie': movie})
