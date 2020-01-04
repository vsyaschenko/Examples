from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Bb

def index(request):
    # #Загружаем шаблон
    # template = loader.get_template('bboard/index.html')
    # #Инициализируем набор записей
    bbs = Bb.objects.all()
    # #Словарь параметров ключ, значение
    # context = {'bbs' : bbs} 
    
    # #Заполняем шаблон и возвращаем готовую страницу
    # return HttpResponse(template.render(context, request))
    return render(request, 'bboard/index.html', {'bbs': bbs})