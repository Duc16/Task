from django.db import models

class Task(models.Model):
    name = models.CharField('Название',max_length=100)
    text = models.TextField('Описание задачи')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'