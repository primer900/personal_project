from django.db import models

# Create your models here.


class Movie(models.Model):
    movie_title = models.CharField(max_length=10)
    rating = models.IntegerField()
    review = models.TextField(max_length=200)
    up_votes = models.DecimalField(default=0, max_digits=3, decimal_places=1)
    down_votes = models.DecimalField(default=0, max_digits=3, decimal_places=1)

    def __str__(self):
        return self.movie_title
