from django.db import models

from distribution.models import Distribution
from users.models import User


class DistributionLog(models.Model):
    sent_time = models.DateTimeField(auto_now_add=True)
    distribution = models.ForeignKey(Distribution, on_delete=models.CASCADE)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    response = models.CharField(max_length=255)
    status_choices = (
        ('success', 'Success'),
        ('failure', 'Failure'),
    )
    status = models.CharField(max_length=10, choices=status_choices)