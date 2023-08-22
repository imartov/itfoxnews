from django.urls import include, path
from .views import *
from rest_framework import routers


app_name="newsApp"

urlpatterns=[
    path('newsposts/', NewsPostAPIList.as_view({"get": "list"})), # get all news http://127.0.0.1:8000/api/newsposts/
    path('newsposts/<int:pk>/', NewsPostAPIList.as_view({"get": "retrieve"})), # get one news http://127.0.0.1:8000/api/newsposts/
    path('newsposts/create/', NewsPostCrateAPIView.as_view()), # create news http://127.0.0.1:8000/api/newsposts/create/
    path('newsposts/update/<int:pk>/', NewsPostUpdateAPIView.as_view({"get": "retrieve", "put": "update"})), # update news http://127.0.0.1:8000/api/newsposts/update/
    path('newsposts/delete/<int:pk>/', NewsPostDeleteAPIView.as_view({"get": "retrieve", "delete": "destroy"})), # create news http://127.0.0.1:8000/api/newsposts/delete/

#    path('getcomments/', NewsPostsView.as_view()), # get comments for news
#    path('addcomment/', NewsPostsView.as_view()), # add comment for news
#    path('deletecomment/', NewsPostsView.as_view()), # delete comment
]