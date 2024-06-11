from rest_framework import serializers
from django.contrib.auth import get_user_model
from articles.models import Article, Comment
from movies.models import Movie, Cinema
from .models import Avatar


class UserSerializer(serializers.ModelSerializer):
    class MovieUserSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ['id', 'title', 'img_src', 'keywords', 'genre', ]
    
    like_movies = MovieUserSerializer(read_only=True, many=True)

    class ArticleUserSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ['id', 'title',]
    
    article_set = ArticleUserSerializer(read_only=True, many=True)
    class Meta:
        model = get_user_model()
        # fields = ['like_movies']
        fields = '__all__'


class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avatar
        fields = ['image', 'user', 'email', 'job', ]
        read_only_fields = ['user', ]