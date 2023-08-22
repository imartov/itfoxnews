from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins, permissions
from rest_framework.viewsets import GenericViewSet
from rest_framework.authentication import (TokenAuthentication,
                                           SessionAuthentication,
                                           BasicAuthentication)
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import *
from .serializers import *
from .permissions import *
from .pagination import *

class NewsPostAPIList(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      GenericViewSet):
    queryset = NewsPost.objects.all()
    serializer_class = NewsPostDisplaySerializer
    pagination_class = AllNewsPostPagination
    # permission_classes = (permissions.IsAuthenticated, ) # if need only authenticated users
    # authentication_classes = (BasicAuthentication, TokenAuthentication, SessionAuthentication, JWTAuthentication) # exclude excess


class NewsPostCrateAPIView(generics.CreateAPIView):
    queryset = NewsPost.objects.all()
    serializer_class = NewsPostCreateSerializer
    permission_classes = (IsAuthenticatedOrAdmin, )
    # authentication_classes = (BasicAuthentication, TokenAuthentication, SessionAuthentication, JWTAuthentication) # exclude excess


class NewsPostUpdateAPIView(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            GenericViewSet):
    queryset = NewsPost.objects.all()
    serializer_class = NewsPostUpdateSerializer
    permission_classes = (IsOwnerOrAdmin, )
    # authentication_classes = (BasicAuthentication, TokenAuthentication, SessionAuthentication, JWTAuthentication) # exclude excess


class NewsPostDeleteAPIView(mixins.RetrieveModelMixin,
                            mixins.DestroyModelMixin,
                            GenericViewSet):
    queryset = NewsPost.objects.all()
    serializer_class = NewsPostDisplaySerializer
    permission_classes = (IsOwnerOrAdmin, )
    # authentication_classes = (BasicAuthentication, TokenAuthentication, SessionAuthentication, JWTAuthentication) # exclude excess



# class NewsPostViewSet(viewsets.ModelViewSet):
#     queryset = NewsPost.objects.all()
#     serializer_class = NewsPostSerializer


# class NewsPostsApiList(generics.ListCreateAPIView):
#     queryset = NewsPost.objects.all()
#     serializer_class = NewsPostSerializer


# class NewPostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = NewsPost.objects.all()
#     serializer_class = NewsPostSerializer


# class NewsPostsView(APIView):
#     def get (self, request):
#         newsposts = NewsPost.objects.all()
#         serializer = NewsPostSerializer(newsposts, many=True)
#         return Response({"newsposts": serializer.data})
   
#     def post(self, request):
#         newspost = request.data.get('newspost')
#         serializer = NewsPostSerializer(data=newspost)
#         if serializer.is_valid(raise_exception=True):
#             saved_newspost = serializer.save()
#         return Response({"success": "News post '{}' created successfully".format(saved_newspost.title)})


# class NewsPostDetailView(APIView):
#     def get (self, request, pk):
#         newspost = get_object_or_404(NewsPost.objects.all(), pk=pk)
#         serializer = NewsPostSerializer(newspost, many=False)
#         return Response({"newspost": serializer.data})

#     def put(self, request, pk):
#         saved_newspost = get_object_or_404(NewsPost.objects.all(), pk=pk)
#         serializer = NewsPostSerializer(instance=saved_newspost, data=request.data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             newspost_saved = serializer.save()
#         return Response({"success": "News post '{}' updated successfully".format(newspost_saved.title)})
    
#     def delete(self, request, pk):
#         newspost = get_object_or_404(NewsPost.objects.all(), pk=pk)
#         newspost_title = newspost.title
#         newspost.delete()
#         return Response({"message": "News post with title `{}` has been deleted.".format(newspost_title)},status=204)
