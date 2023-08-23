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
    serializer_class = NewsPostCreateSerializer
    pagination_class = AllNewsPostPagination
    permission_classes = (permissions.IsAuthenticated, ) # if need only authenticated users
    # authentication_classes = (BasicAuthentication, TokenAuthentication, SessionAuthentication, JWTAuthentication) # exclude excess

    def create(self, request, *args, **kwargs):
        serializer = NewsPostCreateSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(author=self.request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

class NewsPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewsPost.objects.all()
    serializer_class = NewsPostCreateSerializer
    liikup_field = 'id' # slug
    permission_classes = (IsOwnerOrAdmin, )
    # authentication_classes = (BasicAuthentication, TokenAuthentication, SessionAuthentication, JWTAuthentication) # exclude excess
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        if instance:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'Message': 'No News Post Found'}, status=status.HTTP_404_NOT_FOUND)


# class NewsPostAPIList(mixins.ListModelMixin,
#                       mixins.RetrieveModelMixin,
#                       GenericViewSet):
#     queryset = NewsPost.objects.all()
#     serializer_class = NewsPostCreateSerializer
#     # serializer_class = NewsPostDisplaySerializer
#     pagination_class = AllNewsPostPagination
#     # permission_classes = (permissions.IsAuthenticated, ) # if need only authenticated users
#     # authentication_classes = (BasicAuthentication, TokenAuthentication, SessionAuthentication, JWTAuthentication) # exclude excess


# class NewsPostCrateAPIView(generics.CreateAPIView):
#     queryset = NewsPost.objects.all()
#     serializer_class = NewsPostCreateSerializer
#     # serializer_class = NewsPostCreateSerializer
#     permission_classes = (IsAuthenticatedOrAdmin, )
#     # authentication_classes = (BasicAuthentication, TokenAuthentication, SessionAuthentication, JWTAuthentication) # exclude excess


class NewsPostUpdateAPIView(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            GenericViewSet):
    queryset = NewsPost.objects.all()
    serializer_class = NewsPostSerializer
    permission_classes = (IsOwnerOrAdmin, )
    # authentication_classes = (BasicAuthentication, TokenAuthentication, SessionAuthentication, JWTAuthentication) # exclude excess


class NewsPostDeleteAPIView(mixins.RetrieveModelMixin,
                            mixins.DestroyModelMixin,
                            GenericViewSet):
    queryset = NewsPost.objects.all()
    serializer_class = NewsPostSerializer
    permission_classes = (IsOwnerOrAdmin, )
    # authentication_classes = (BasicAuthentication, TokenAuthentication, SessionAuthentication, JWTAuthentication) # exclude excess