from django.urls import include, path
from .views import *
from rest_framework import routers


app_name="newsApp"

urlpatterns=[
    # NewsPosts
    path('newsposts/', NewsPostListCreateView.as_view(), name='newsposts'), # http://127.0.0.1:8000/api/newsposts/
    path('newsposts/<int:pk>/', NewsPostDetailView.as_view(), name='newsposts'), # http://127.0.0.1:8000/api/newsposts/newspost_id/

    # Comments
    path("comment_list/newspost/<int:newspost_id>/", CommentListCreateView.as_view(), name="newspost_comment_list"), # http://127.0.0.1:8000/api/comment_list/newspost/newspost_id/
    path("newsposts/<int:newspost_id>/comment/<int:comment_id>/", CommentDetailView.as_view(), name="newspost_comment_detail"), # http://127.0.0.1:8000/api/newsposts/newspost_id/comment/comment_id/

    # Likes
    path('likes/create/<int:newspost_id>/', LikeListCreateView.as_view(), name='like-create'), # http://127.0.0.1:8000/api/likes/create/newspost_id/
    path('likes/delete/<int:pk>/', LikeDeleteView.as_view(), name='like-delete'), # http://127.0.0.1:8000/api/likes/delete/id/
]