from django.db import models

# модель описывает структуру таблицы базы данных
# атрибуты модели являются полями
# поле id фржймворк создает автоматически
class Bb(models.Model):
    title = models.CharField(max_length=50) #строка фикс. длины
    content = models.TextField(null=True, blank=True)#строка неогранич. длины
    price = models.FloatField(null=True, blank=True)#вещественное число
    published = models.DateTimeField(auto_now_add=True, db_index=True)#дата время
