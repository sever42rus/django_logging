from email.policy import default
from pyexpat import model
from django.contrib.auth.models import User
from django.db import models
from .choices import *

# Create your models here.


class LoggingModel(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, related_name='model_changes',
                             verbose_name='Пользователь', null=True)
    model_name = models.CharField(max_length=200, verbose_name='измененная модель')
    record_id = models.PositiveBigIntegerField(verbose_name='ID записи')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания записи')
    data = models.JSONField(blank=True, verbose_name='информация', default=dict)
    action = models.SmallIntegerField(choices=LOGGING_ACTIONS)
