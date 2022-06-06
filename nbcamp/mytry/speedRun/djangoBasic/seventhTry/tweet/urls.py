from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('tweet/', views.tweet, name='tweet'),
    path('tweet/delete/<int:id>', views.delete_tweet, name='delete-tweet'),
    path('tweet/<int:id>', views.view_tweet, name='view_tweet'),
    path('tweet/comment/<int:id>', views.comment, name='comment'),
    path('tweet/comment/delete/<int:id>', views.delete_comment, name='delete-comment'),
]