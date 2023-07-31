from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Message(models.Model):
    subject = models.TextField(verbose_name='тема письма')
    body = models.TextField(**NULLABLE, verbose_name='тело письма')


class Distribution(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    frequency_choices = (
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    )
    frequency = models.CharField(max_length=10, choices=frequency_choices)
    status_choices = (
        ('created', 'Created'),
        ('started', 'Started'),
        ('completed', 'Completed'),
    )
    status = models.CharField(max_length=10, choices=status_choices)
