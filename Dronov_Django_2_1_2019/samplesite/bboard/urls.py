from django.urls import path

from .views import index, by_rubric, BbCreateView

#Ссылки
urlpatterns = [
    #аргумент name содержит имя используемое в шаблонах для тега url
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),#Главная вызывает метод index
    path('add/', BbCreateView.as_view(), name='add')
]