from django.urls import path
from .views import *


app_name="newsApp"

urlpatterns=[
    path('newsposts/', NewsPostsView.as_view()), # list of all news
    path('newsposts/<int:pk>/', NewsPostDetailView.as_view()), # update news post
#    path('gettoken/', NewsPostsView.as_view()), # get token for user
#    path('updatenews/', NewsPostsView.as_view()), # update news
#    path('deletenews/', NewsPostsView.as_view()), # deletenews
#    path('getcomments/', NewsPostsView.as_view()), # get comments for news
#    path('addcomment/', NewsPostsView.as_view()), # add comment for news
#    path('deletecomment/', NewsPostsView.as_view()), # delete comment
]