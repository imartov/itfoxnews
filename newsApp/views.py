from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics, mixins, permissions, status
from rest_framework.viewsets import GenericViewSet
from rest_framework.authentication import (TokenAuthentication,
                                           SessionAuthentication,
                                           BasicAuthentication)
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import *
from .serializers import *
from .permissions import *
from .pagination import *


class NewsPostListCreateView(generics.ListCreateAPIView):
    queryset = NewsPost.objects.all()
    serializer_class = NewsPostSerializer
    pagination_class = AllNewsPostPagination
    # permission_classes = (permissions.IsAuthenticated, ) # if need only authenticated users
    # authentication_classes = (BasicAuthentication, TokenAuthentication, SessionAuthentication, JWTAuthentication) # exclude excess

    def create(self, request, *args, **kwargs):
        # TODO: проверка аутентификации check_object_permissions
        serializer = NewsPostSerializer(data=request.data, context={'request': request})
        if not request.user.is_authenticated:
            raise serializers.ValidationError({"Message": "You must be logged in to leave a news post"})
        serializer.is_valid(raise_exception=True)
        serializer.save(author=self.request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

class NewsPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewsPost.objects.all()
    serializer_class = NewsPostSerializer
    liikup_field = 'id' # slug
    # permission_classes = (IsOwnerOrAdmin, )
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
            raise serializers.ValidationError({"Message": "You must be logged in to delete this news post"})
        if newspost.author.is_staff != request.user.is_staff:
            raise serializers.ValidationError({"Message": "You are not authorized to perform this action"})
        return super().delete(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        newspost = self.get_object()
        if not request.user.is_authenticated:
            raise serializers.ValidationError({"Message": "You must be logged in to delete this news post"})
        if newspost.author.is_staff != request.user.is_staff:
            raise serializers.ValidationError({"Message": "You are not authorized to perform this action"})
        return super().put(request, *args, **kwargs)
        

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = (permissions.IsAuthenticated, )
    
    def get_queryset(self):
        newspost_id = self.kwargs.get('newspost_id')
        return Comment.objects.filter(newspost_id=newspost_id)
    
    def perform_create(self, serializer):
        newspost_id = self.kwargs.get('newspost_id')
        newspost = get_object_or_404(NewsPost, id=newspost_id)
        if Comment.objects.filter(newspost=newspost, author=self.request.user).exists():
            raise serializers.ValidationError({'Message': 'You have already added comment on this news post'})
        if not self.request.user.is_authenticated:
            raise serializers.ValidationError({"Message": "You must be logged in to leave a comment"})
        serializer.save(author=self.request.user, newspost=newspost)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = (IsOwnerOrAdmin, )
    
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
        if newspost.author != request.user or comment.author.is_staff != request.user.is_staff:
            raise serializers.ValidationError({"Message": "You are not authorized to perform this action"})
        return super().delete(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        comment = self.get_object()
        if comment.author != request.user or comment.author.is_staff != request.user.is_staff:
            raise serializers.ValidationError({"Message": "You are not authorized to perform this action"})
        return super().put(request, *args, **kwargs)
