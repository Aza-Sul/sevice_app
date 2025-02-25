from django.core.validators import MaxValueValidator
from django.db import models

from clients.models import Client


class Service(models.Model):
    name = models.CharField('Название сервиса', max_length=50)
    full_price = models.PositiveIntegerField('Цена')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сервис"
        verbose_name_plural = "Сервисы"


class Plan(models.Model):
    PLAN_TYPES = (
        ('full', 'Full'),
        ('student', 'Student'),
        ('discount', 'Discount'),
    )
    plan_type = models.CharField('Тип плана', choices=PLAN_TYPES, max_length=10)
    discount_percent = models.PositiveIntegerField('Процент скидки', default=0, validators=[MaxValueValidator(100)])

    def __str__(self):
        return self.plan_type

    class Meta:
        verbose_name = "План"
        verbose_name_plural = "Планы"


class Subscription(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='subscriptions')
    service = models.ForeignKey(Service, on_delete=models.PROTECT, related_name='subscriptions')
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT, related_name='subscriptions')

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
