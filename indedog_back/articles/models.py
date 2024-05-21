from django.db import models
from django.conf import settings
from movies.models import Movie, Cinema

# Create your models here.
class Article(models.Model):
    # movie = models.ForeignKey(Movie, on_delete=models.CASCADE, blank=True)
    # cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_notice = models.BooleanField(default=False)
    category = models.CharField(max_length=20)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    point = models.FloatField(default=0.0)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, null=True)
    content = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
