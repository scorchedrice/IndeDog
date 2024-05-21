from rest_framework import serializers
from .models import Article, Comment
from movies.models import Movie, Cinema


class ArticleSerializer(serializers.ModelSerializer):
    class ArticleCommentSerializer(serializers.ModelSerializer):
        user = serializers.ReadOnlyField(source='user.username')
        class Meta:
            model = Comment
            fields = ('content', 'user')

    user = serializers.ReadOnlyField(source='user.username')
    comment_set = ArticleCommentSerializer(read_only=True, many=True)
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user', )


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Comment
        fields = ('content', 'point', 'article', 'user')
        read_only_fields = ('user', 'article', 'cinema', 'movie')
        

class CommentMovieSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Comment
        fields = ('content', 'point', 'movie', 'user')
        read_only_fields = ('user', 'article', 'cinema', 'movie')


# class NoticeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = '__all__'
#         read_only_fields = 