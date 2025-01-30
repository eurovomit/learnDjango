from django.urls import path
from django.views.generic import TemplateView

from learnDjango import views


urlpatterns = [path("", views.index, name="index"),
               path("about/", TemplateView.as_view(template_name="learnDjango/about.html", extra_context={"header": "о сайте"}))]
