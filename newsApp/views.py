from django.shortcuts import get_object_or_404, render

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import NewsPostSerializer


class NewsPostsView(APIView):
    def get (self, request):
        newsposts = NewsPost.objects.all()
        serializer = NewsPostSerializer(newsposts, many=True)
        return Response({"newsposts": serializer.data})
   
    def post(self, request):
        newspost = request.data.get('newspost')
        serializer = NewsPostSerializer(data=newspost)
        if serializer.is_valid(raise_exception=True):
            saved_newspost = serializer.save()
        return Response({"success": "News post '{}' created successfully".format(saved_newspost.title)})


class NewsPostDetailView(APIView):
    def get (self, request, pk):
        newspost = get_object_or_404(NewsPost.objects.all(), pk=pk)
        serializer = NewsPostSerializer(newspost, many=False)
        return Response({"newspost": serializer.data})

    def put(self, request, pk):
        saved_newspost = get_object_or_404(NewsPost.objects.all(), pk=pk)
        serializer = NewsPostSerializer(instance=saved_newspost, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            newspost_saved = serializer.save()
        return Response({"success": "News post '{}' updated successfully".format(newspost_saved.title)})
    
    def delete(self, request, pk):
        newspost = get_object_or_404(NewsPost.objects.all(), pk=pk)
        newspost_title = newspost.title
        newspost.delete()
        return Response({"message": "News post with title `{}` has been deleted.".format(newspost_title)},status=204)
