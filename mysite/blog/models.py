from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset().filter(status='published')


class Post(models.Model):
    objects = models.Manager()
    published = PublishedManager()
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_posts')
    creator = models.CharField(max_length=50, default='')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              default='draft')
    rating = models.IntegerField(default=0)

    def first_sentence(self):
        punctuation = []
        if '.' in self.body:
            punctuation.append(self.body.index("."))
        if '!' in self.body:
            punctuation.append(self.body.index("!"))
        if '?' in self.body:
            punctuation.append(self.body.index("?"))

        minimum_punctuation = min(punctuation)
        return self.body.partition(self.body[minimum_punctuation])[0] + \
            self.body.partition(self.body[minimum_punctuation])[1]

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[
                           self.publish.year,
                           self.publish.strftime('%m'),
                           self.publish.strftime('%d'),
                           self.slug])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
