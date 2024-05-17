from django.db import models
from django.conf import settings

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)
    img_src = models.CharField(max_length=100)
    age = models.TextField()
    director = models.TextField()
    keywords = models.TextField()
    length = models.CharField(max_length=20)
    genre = models.TextField()
    making_year = models.CharField(max_length=10)
    detail = models.TextField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    cinemas = models.TextField()


class Cinema(models.Model):
    recent_movies = models.ManyToManyField(Movie, related_name='recent_cinemas')
    address = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
