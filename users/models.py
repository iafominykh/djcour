from django.db import models

NULLABLE = {'null': True, 'blank': True}


# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=250, verbose_name='Адрес электронной почты')
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    image = models.ImageField(upload_to='users/', **NULLABLE, verbose_name='Изображение')
    comment = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return f'{self.full_name}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
