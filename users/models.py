from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """Модель пользователя с расширенными полями"""
    ROLE_CHOICES = [
        ('manager', 'Руководитель'),
        ('employee', 'Сотрудник')
    ]
    department = models.ForeignKey(
        'Department', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        verbose_name="Отдел"
    )
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


class Company(models.Model):
    """Модель компании"""
    name = models.CharField(verbose_name='Название компании', max_length=255, unique=True)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    leader = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='companies_led',
        verbose_name="Руководитель компании"
    )
    founded_year = models.PositiveIntegerField(verbose_name="Год основания", null=True, blank=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    """Модель отделов"""
    title = models.CharField(verbose_name='Название отдела', max_length=100, unique=True)
    company = models.ForeignKey(
        Company, 
        on_delete=models.CASCADE, 
        verbose_name='Компания', 
        blank=True, 
        null=True
    )
    leader = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='departments_led',
        verbose_name="Руководитель отдела"
    )

    def __str__(self):
        return f"{self.title} ({self.company.name if self.company else 'Нет компании'})"