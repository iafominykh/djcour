from django.db import models

NULLABLE = {'null': True, 'blank': True}


# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=250, verbose_name='Адрес электронной почты')
    surname = models.CharField(max_length=200, verbose_name='Фамилия')
    name = models.CharField(max_length=200, verbose_name='Имя')
    patronymic = models.CharField(**NULLABLE, max_length=200, verbose_name='Отчество')
    comment = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
