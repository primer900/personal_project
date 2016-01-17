from django.contrib import admin
from .models import Movie
# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    list_display = ('movie_title', 'rating', 'review')

    list_filter = ('movie_title', 'rating')
    search_fields = ('movie_title', 'rating')

admin.site.register(Movie, MovieAdmin)
