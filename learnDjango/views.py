from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')

def user(request):
    age = request.GET.get('age', 0)
    name = request.GET.get('name', 'undefined')
    return HttpResponse(f'Имя: {name} Возраст: {age}')
