from django.db import models

class Bb(models.Model):
    #Класс Bb = Таблица БД Bb
    #Объявленные переменные = поля таблицы
    title = models.CharField(max_length=50, 
                                verbose_name='Товар')
    content = models.TextField(null=True, 
                                blank=True, 
                                verbose_name='Описание')
    price = models.FloatField(null=True, 
                                blank=True, 
                                verbose_name='Цена')
    rubric = models.ForeignKey('Rubric', #Передается ссылка на класс, если класс объявлен раньше текущего
                                null=True,
                                on_delete=models.PROTECT, #Защита от каскадного удаления (при удалении рубрики не удалять подчиненные объявления)
                                verbose_name='Рубрика')
    published = models.DateTimeField(auto_now_add=True, 
                                db_index=True, 
                                verbose_name='Опубликовано')
    class Meta:
        #Параметры отображения модели на странице
        #Представление списка, записи и сортировка списка
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']#действует везде для модели

class Rubric(models.Model):
    name = models.CharField(max_length=20, 
                            db_index=True, #Индексация вкл.
                            verbose_name = 'Название')
    def __str__(self):
        #Переопределяем строковое представление класса
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']