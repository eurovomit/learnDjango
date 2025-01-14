from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotFound


def index(request, id):
    people = [None, "Bob", "Sam", "Tom"]
    if id in range(1, len(people)):
        return HttpResponse(people[id])
    else:
        return HttpResponseNotFound("Not found")

def about(request):
    return HttpResponse('about')

def contact(request):
    return HttpResponseRedirect('/about')

def details(request):
    return HttpResponsePermanentRedirect('/')

