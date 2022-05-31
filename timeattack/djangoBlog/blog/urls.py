from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new_article, name='new-article'),
    path('categories/', views.view_categories, name='view-categories')
]