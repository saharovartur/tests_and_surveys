from django.db import models
from users.models import CustomUser

class Test(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название теста")
    description = models.TextField(null=True, blank=True, verbose_name="Описание теста")
    created_by = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.CASCADE, 
        related_name='tests_created', 
        verbose_name="Автор теста"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    recipient_email = models.EmailField(verbose_name="Email получателя результатов")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"


class TestQuestion(models.Model):
    test = models.ForeignKey(
        'Test', 
        on_delete=models.CASCADE, 
        related_name='questions', 
        verbose_name="Тест"
    )
    text = models.TextField(verbose_name="Текст вопроса")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Вопрос теста"
        verbose_name_plural = "Вопросы теста"


class TestAnswerOption(models.Model):
    question = models.ForeignKey(
        'TestQuestion', 
        on_delete=models.CASCADE, 
        related_name='options', 
        verbose_name="Вопрос"
    )
    text = models.CharField(max_length=255, verbose_name="Текст варианта")
    is_correct = models.BooleanField(default=False, verbose_name="Правильный ответ")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Вариант ответа"
        verbose_name_plural = "Варианты ответа"


class TestResponse(models.Model):
    test = models.ForeignKey(
        'Test', 
        on_delete=models.CASCADE, 
        related_name='responses', 
        verbose_name="Тест"
    )
    user = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        related_name='test_responses', 
        verbose_name="Сотрудник"
    )
    submitted_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата прохождения")

    def __str__(self):
        return f"Результат {self.user} по тесту {self.test}"

    class Meta:
        verbose_name = "Результат теста"
        verbose_name_plural = "Результаты тестов"


class TestAnswer(models.Model):
    response = models.ForeignKey(
        'TestResponse', 
        on_delete=models.CASCADE, 
        related_name='answers', 
        verbose_name="Результат теста"
    )
    question = models.ForeignKey(
        'TestQuestion', 
        on_delete=models.CASCADE, 
        related_name='answers', 
        verbose_name="Вопрос"
    )
    selected_option = models.ForeignKey(
        'TestAnswerOption', 
        on_delete=models.CASCADE, 
        related_name='selected_in', 
        verbose_name="Выбранный вариант"
    )

    def __str__(self):
        return f"Ответ на вопрос {self.question}"

    class Meta:
        verbose_name = "Ответ на вопрос теста"
        verbose_name_plural = "Ответы на вопросы теста"