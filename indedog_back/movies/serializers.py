from rest_framework import serializers
from .models import Movie, Cinema


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'img_src', 'keywords', 'director', 'cinemas', 'genre', 'title_en', 'making_year', 'length')


class CinemaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = ('address', 'latitude', 'longitude')