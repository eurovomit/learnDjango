from django.urls import path
from learnDjango import views

urlpatterns = [path("", views.index),
               path("about/", views.about, kwargs={'name': 'Tom', 'age': 20}),
               path("contact/", views.contact),
               path('user/<str:name>/<int:age>', views.user),
               path('user/<str:name>/', views.user),
               path('user/', views.user),]