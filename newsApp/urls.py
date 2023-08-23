from django.urls import include, path
from .views import *
from rest_framework import routers


app_name="newsApp"

urlpatterns=[
    path('newsposts/', NewsPostListCreateView.as_view(), name='newsposts'), # http://127.0.0.1:8000/api/newsposts/
    path('newsposts/<int:pk>/', NewsPostDetailView.as_view(), name='newsposts'), # http://127.0.0.1:8000/api/newsposts/

#    path('getcomments/', NewsPostsView.as_view()), # get comments for news
#    path('addcomment/', NewsPostsView.as_view()), # add comment for news
#    path('deletecomment/', NewsPostsView.as_view()), # delete comment
]