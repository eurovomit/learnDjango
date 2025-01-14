from django.urls import path, include
from learnDjango import views


urlpatterns = [path("index/<int:id>", views.index),
               path("about/", views.about),
               path("contact/", views.contact),
               path("details/", views.details),]
