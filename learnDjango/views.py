from django.shortcuts import render
from django.template.response import TemplateResponse


def index(request):
    cat = []
    return render(request, "learnDjango/index.html", context={"cat": cat})
