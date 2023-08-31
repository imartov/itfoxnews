from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics, mixins, permissions, status
from rest_framework.viewsets import GenericViewSet
from rest_framework.authentication import (TokenAuthentication,
                                           SessionAuthentication,
                                           BasicAuthentication)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *
from .permissions import *
from .pagination import *


class NewsPostListCreateView(generics.ListCreateAPIView):
    queryset = NewsPost.objects.all()
    serializer_class = NewsPostSerializer
    pagination_class = AllNewsPostPagination
    # authentication_classes = (BasicAuthentication, TokenAuthentication, SessionAuthentication, JWTAuthentication) # exclude excess

    def create(self, request, *args, **kwargs):
        serializer = NewsPostSerializer(data=request.data, context={'request': request})
        self.check_object_permissions(self.request, obj=None)
        if not request.user.is_authenticated:
            raise serializers.ValidationError({"Message": "You must be logged in to post"})
        serializer.is_valid(raise_exception=True)
        serializer.save(author=self.request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

class NewsPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewsPost.objects.all()
    serializer_class = NewsPostSerializer
    liikup_field = 'id' # slug
    # authentication_classes = (BasicAuthentication, TokenAuthentication, SessionAuthentication, JWTAuthentication) # exclude excess
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        if instance:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'Message': 'No News Post Found'}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, *args, **kwargs):
        newspost = self.get_object()
        if not request.user.is_authenticated:
            raise serializers.ValidationError({"Message": "You must be logged in to delete post"})
        if newspost.author != request.user and not request.user.is_staff:
            raise serializers.ValidationError({"Message": "You are not authorized to perform this action"})
        return super().delete(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        newspost = self.get_object()
        if not request.user.is_authenticated:
            raise serializers.ValidationError({"Message": "You must be logged in to update post"})
        if newspost.author != request.user and not request.user.is_staff:
            raise serializers.ValidationError({"Message": "You are not authorized to perform this action"})
        return super().put(request, *args, **kwargs)
        

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        newspost_id = self.kwargs.get('newspost_id')
        return Comment.objects.filter(newspost_id=newspost_id)
    
    def perform_create(self, serializer):
        newspost_id = self.kwargs.get('newspost_id')
        newspost = get_object_or_404(NewsPost, id=newspost_id)
        if not self.request.user.is_authenticated:
            raise serializers.ValidationError({"Message": "You must be logged in to leave a comment"})
        if Comment.objects.filter(newspost=newspost, author=self.request.user).exists():
            raise serializers.ValidationError({'Message': 'You have already added comment on this news post'})
        self.check_object_permissions(self.request, obj=None)
        serializer.save(author=self.request.user, newspost=newspost)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    def get_object(self):
        comment_id = self.kwargs.get('comment_id')
        comment = get_object_or_404(Comment, id = comment_id)
        
        newspost_id = self.kwargs.get("newspost_id")
        if comment.newspost_id != newspost_id:
            raise serializers.ValidationError({"Message": "This comment is not related to the requested blog"})
        return comment
    
    def delete(self, request, *args, **kwargs):
        comment = self.get_object()
        newspost = get_object_or_404(NewsPost, id=comment.newspost_id)
        if not self.request.user.is_authenticated:
            raise serializers.ValidationError({"Message": "You must be logged in to delete comment"})
        if comment.author != request.user and newspost.author != request.user and not request.user.is_staff:
            raise serializers.ValidationError({"Message": "You are not authorized to perform this action"})
        return super().delete(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        comment = self.get_object()
        if not self.request.user.is_authenticated:
            raise serializers.ValidationError({"Message": "You must be logged in to update comment"})
        if comment.author != request.user:
            raise serializers.ValidationError({"Message": "You are not authorized to perform this action"})
        return super().put(request, *args, **kwargs)
    

class LikeListCreateView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        newspost_id = self.kwargs.get('newspost_id')
        newspost = get_object_or_404(NewsPost, id=newspost_id)
        if not self.request.user.is_authenticated:
            raise serializers.ValidationError({"Message": "You must be logged in to like"})
        serializer.save(user=self.request.user, newspost=newspost)


class LikeDeleteView(generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def delete(self, request, *args, **kwargs):
        like = self.get_object()
        if not self.request.user.is_authenticated:
            raise serializers.ValidationError({"Message": "You must be logged in to delete like"})
        if like.user != request.user:
            raise serializers.ValidationError({"Message": "You are not authorized to perform this action"})
        return super().delete(request, *args, **kwargs)
