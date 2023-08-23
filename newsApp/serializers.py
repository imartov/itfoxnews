from rest_framework import serializers
from django.urls import reverse
from .models import *


class CommentSerializer(serializers.ModelSerializer):
    newspost = serializers.StringRelatedField(read_only=True)
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Comment
        fields = "__all__"


class NewsPostSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = NewsPost
        fields = "__all__"   

    def get_comments(self, obj):
        comments = Comment.objects.filter(newspost=obj)[:10]
        request = self.context.get('request')
        return {
            "comments": CommentSerializer(comments, many=True).data,
            "all_comment_link": request.build_absolute_uri(reverse('newsApp:newspost_comment_list', kwargs={'newspost_id': obj.id}))
        }
