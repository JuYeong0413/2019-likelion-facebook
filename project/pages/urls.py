from django.urls import path
from . import views

urlpatterns = [
    path('newsfeed/', views.newsfeed, name="newsfeed"),
    path('write/', views.write, name="write"),
    path('success/', views.success, name="success"),
    path('create_comment/', views.create_comment, name="create_comment"),
]