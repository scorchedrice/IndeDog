from rest_framework import serializers
from .models import Article, Comment


class ArticleSerializer(serializers.ModelSerializer):
    class CommentArticleSerializer(serializers.ModelSerializer):
        user = serializers.ReadOnlyField(source='user.username')
        class Meta:
            model = Comment
            fields = ('content', 'user')

    user = serializers.ReadOnlyField(source='user.username')
    comment_set = CommentArticleSerializer(read_only=True, many=True)
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user', )


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Comment
        fields = ('content', 'point', 'article', 'user')
        read_only_fields = ('user', 'article', 'cinema')


# class NoticeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = '__all__'
#         read_only_fields = 