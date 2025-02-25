from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    company_name = models.CharField('Название компании', max_length=100)
    full_address = models.CharField('Адрес клиента', max_length=100)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
