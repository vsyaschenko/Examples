from django.contrib import admin

from .models import Bb, Rubric


class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric')#Поля формы списка
    list_display_links = ('title', 'content')#Ссылочные поля списка
    search_fields = ('title', 'content', )#Поля по которым осуществляется поиск

#Регистрация моделей
admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)