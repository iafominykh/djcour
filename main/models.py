from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Customer(models.Model):
    email = models.EmailField(max_length=100, verbose_name='Контактный email')
    fullname = models.CharField(max_length=150, verbose_name='ФИО')
    comment = models.TextField(verbose_name='Комментарий', **NULLABLE)
    created_by = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Создатель', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='Активность')

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Message(models.Model):
    subject = models.CharField(max_length=150, verbose_name='Тема письма')
    body = models.TextField(verbose_name='Тело сообщения')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return self.subject


class Mailing(models.Model):
    ONCE = 'раз'
    DAILY = 'раз в день'
    WEEKLY = 'раз в неделю'
    MONTHLY = 'раз в месяц'

    FREQUENCY_CHOICES = [
        (ONCE, 'раз'),
        (DAILY, 'раз в день'),
        (WEEKLY, 'раз в неделю'),
        (MONTHLY, 'раз в месяц'),
    ]

    CREATED = 'Создана'
    LAUNCHED = 'Запущена'
    COMPLETED = 'Завершена'

    SELECT_STATUS = [
        (CREATED, 'Создана'),
        (LAUNCHED, 'Запущена'),
        (COMPLETED, 'Завершена'),
    ]

    mailing_time = models.TimeField(verbose_name='Время рассылки')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Сообщение')
    frequency = models.CharField(max_length=100, choices=FREQUENCY_CHOICES, verbose_name='Периодичность')
    status = models.CharField(max_length=50, default=CREATED, choices=SELECT_STATUS, verbose_name='Статус рассылки')
    created_by = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Создатель', **NULLABLE)
    customer = models.ManyToManyField(Customer, verbose_name='Клиент рассылки')


    def __str__(self):
        return self.message.subject

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Attempt(models.Model):
    DELIVERED = 'доставлено'
    NOT_DELIVERED = 'не доставлено'

    SELECT_STATUS = (
        (DELIVERED, 'доставлено'),
        (NOT_DELIVERED, 'не доставлено'),
    )

    time_mailing = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время последней попытки')
    status = models.CharField(choices=SELECT_STATUS, verbose_name='Статус попытки')
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Рассылка')
    server_response = models.TextField(**NULLABLE, verbose_name='Ответ почтового сервера')

    def __str__(self):
        return self.mailing.message.subject

    class Meta:
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистики'
