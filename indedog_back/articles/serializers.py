from rest_framework import serializers
from .models import Article, Comment
from movies.models import Movie, Cinema


class ArticleSerializer(serializers.ModelSerializer):
    class ArticleCommentSerializer(serializers.ModelSerializer):
        user = serializers.ReadOnlyField(source='user.username')
        class Meta:
            model = Comment
            fields = ('id', 'content', 'user', 'like_users')

    user = serializers.ReadOnlyField(source='user.username')
    comment_set = ArticleCommentSerializer(read_only=True, many=True)
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user', 'like_users')


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Comment
        fields = ('id', 'content', 'point', 'article', 'user', 'like_users')
        read_only_fields = ('user', 'article', 'cinema', 'movie', 'like_users')
        

class CommentMovieSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Comment
        fields = ('id', 'content', 'point', 'movie', 'user', 'like_users')
        read_only_fields = ('user', 'article', 'cinema', 'movie', 'like_users')


class CommentCinemaSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Comment
        fields = ('id', 'content', 'point', 'cinema', 'user', 'like_users')
        read_only_fields = ('user', 'article', 'cinema', 'movie', 'like_users')


class ArticleLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('like_users',)

# class NoticeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = '__all__'
#         read_only_fields = 