from django.shortcuts import render
from django.http import HttpResponse

from .models import Bb

def index(request):
    s = 'Список объявлений'+'\r\n'*3
    for bb in Bb.objects.order_by('-published'):
        s += bb.title + '\r\n' + bb.content + '\r\n'*2
    return HttpResponse(s, content_type='text/plain; charset=utf-8')
