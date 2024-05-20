from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user', )


# class NoticeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = '__all__'
#         read_only_fields = 