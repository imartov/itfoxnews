from rest_framework import serializers
from django.urls import reverse
from .models import *


class CommentSerializer(serializers.ModelSerializer):
    newspost = serializers.StringRelatedField(read_only=True)
    author = serializers.ReadOnlyField(source='author.username')
    # detail_link = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = "__all__"

    # def get_detail_link(self, obj):
    #     request = self.context.get('request')
    #     return request.build_absolute_uri(reverse('newsApp:newspost_comment_detail',
    #                                             kwargs={'newspost_id': obj.newspost_id,
    #                                             "comment_id": obj.id}))


class NewsPostSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = NewsPost
        fields = "__all__"   

    def get_comments(self, obj):
        comments = Comment.objects.filter(newspost=obj)[:10]
        comments_count = Comment.objects.filter(newspost=obj).count()
        request = self.context.get('request')
        return {
            "comments": CommentSerializer(comments, many=True).data,
            "all_comment_link": request.build_absolute_uri(reverse('newsApp:newspost_comment_list', kwargs={'newspost_id': obj.id})),
            "comments_count": comments_count
        }
