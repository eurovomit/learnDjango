from django.shortcuts import render
from django.template.response import TemplateResponse


def index(request):
    return render(request, "learnDjango/index.html", context={"site": "javarush"})
