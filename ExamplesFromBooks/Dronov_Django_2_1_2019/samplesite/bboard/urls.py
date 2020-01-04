from django.urls import path

from .views import index

#Ссылки
urlpatterns = [
    path('', index)#Главная вызывает метод index
]