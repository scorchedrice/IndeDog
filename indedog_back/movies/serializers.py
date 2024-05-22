from rest_framework import serializers
from .models import Movie, Cinema
from articles.models import Comment
from django.contrib.auth import get_user_model 


class MovieListSerializer(serializers.ModelSerializer):
    class MovieCommentSerializer(serializers.ModelSerializer):
        user = serializers.ReadOnlyField(source='user.username')
        class Meta:
            model = Comment
            fields = ('id', 'content', 'user', 'point', 'like_users')
    
    comment_set = MovieCommentSerializer(read_only=True, many=True)
    class Meta:
        model = Movie
        fields = ('id', 'title', 'img_src', 'keywords', 'director', 'cinemas', 'genre', 'title_en', 'making_year', 'length', 'comment_set', 'like_users')
        # fields = '__all__'


class MovieLikeSerializer(serializers.ModelSerializer):
    like_users = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all(),
        many=True,
        required=False
    )
    class Meta:
        model = Movie
        fields = ('like_users',)

    def update(self, instance, validated_data):
        like_users_data = validated_data.pop('like_users', [])
        instance.like_users.set(like_users_data)
        return instance


class CinemaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = ('address', 'latitude', 'longitude', 'recent_movies')
        read_only_fields = ('recent_movies', )

