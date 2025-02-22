from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('manager', 'Руководитель'),
        ('employee', 'Сотрудник')
    ]
    department = models.CharField(max_length=255, null=True, blank=True, verbose_name="Отдел")
    manager = models.ForeignKey(
        'self', 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True, 
        related_name='subordinates', 
        verbose_name="Руководитель"
    )
    email = models.EmailField(unique=True, verbose_name="Email")
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='employee', verbose_name="Роль")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"