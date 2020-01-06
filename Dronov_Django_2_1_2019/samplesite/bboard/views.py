from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Bb, Rubric

def index(request):
    # #Загружаем шаблон
    # template = loader.get_template('bboard/index.html')
    # #Инициализируем переменные
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    # #Словарь параметров ключ, значение
    # context = {'bbs' : bbs} 
    
    # #Заполняем шаблон и возвращаем готовую страницу
    # return HttpResponse(template.render(context, request))
    return render(request, 'bboard/index.html', context)

def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 
                'rubrics': rubrics,
                'current_rubric': current_rubric}
    return render(request, 'bboard/by_rubric.html', context)