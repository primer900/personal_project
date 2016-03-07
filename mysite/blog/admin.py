from django.contrib import admin
from .models import Post
from .models import ReadingList

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


class ReadingListAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'year_published', 'genres')
    list_filter = ('title', 'genres')
    search_fields = ('title',)
    ordering = ['author', 'genres']

admin.site.register(Post, PostAdmin)
admin.site.register(ReadingList, ReadingListAdmin)
