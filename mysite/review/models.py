from django.db import models
from django import forms
# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=10)
    synopsis = models.TextField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.name

