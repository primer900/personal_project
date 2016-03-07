from django.shortcuts import render, get_object_or_404
from .models import Post
from .models import ReadingList
# Create your views here.


def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html',
                  {'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})


def most_recent_list(request):
    posts = Post.published.order_by('publish')[:10]
    return render(request,
                  'blog/post/recent.html',
                  {'posts': posts})


def reading_list(request):
    readings = ReadingList.objects.all()
    return render(request,
                  'blog/reading_list/detail.html',
                  {'readings': readings})

