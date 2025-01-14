from django.urls import path, include
from learnDjango import views


urlpatterns = [path("", views.index),
               path("user/", views.user),]
