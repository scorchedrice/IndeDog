from rest_framework import serializers
from .models import Movie, Cinema
from articles.models import Comment


class MovieListSerializer(serializers.ModelSerializer):
    class MovieCommentSerializer(serializers.ModelSerializer):
        user = serializers.ReadOnlyField(source='user.username')
        class Meta:
            model = Comment
            fields = ('content', 'user', 'point')
    
    comment_set = MovieCommentSerializer(read_only=True, many=True)
    class Meta:
        model = Movie
        fields = ('id', 'title', 'img_src', 'keywords', 'director', 'cinemas', 'genre', 'title_en', 'making_year', 'length', 'comment_set')


class CinemaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = ('address', 'latitude', 'longitude')

