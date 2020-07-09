from django.shortcuts import render
from django.http import HttpResponse

def index(request):
#Функция-контроллер принимает в качестве параметра экземплярк класса HttpRequest
#Возвращает экземпляр класса HttpResponse
    return HttpResponse('Здесь будет список объявлений')


