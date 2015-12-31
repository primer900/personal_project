from django.contrib import admin
from .models import Movie
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    fieldsets = [
        ('rating', {'fields': ['rating']}),
    ]
    list_display = ('name', 'synopsis', 'rating')
    list_filter = ['rating']
    search_fields = ['name']

admin.site.register(Movie, MovieAdmin)
