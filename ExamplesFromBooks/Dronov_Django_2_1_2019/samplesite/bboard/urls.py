from django.urls import path

from .views import index, by_rubric

#Ссылки
urlpatterns = [
    path('<int:rubric_id>/', by_rubric),
    path('', index)#Главная вызывает метод index
]