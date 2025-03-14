from django.db import models
from users.models import CustomUser

class Survey(models.Model):
    """
    Модель опроса.
    Представляет собой опрос, который может быть создан автором и привязан к компании или отделу.
    """
    title = models.CharField(max_length=255, verbose_name="Название опроса")
    description = models.TextField(null=True, blank=True, verbose_name="Описание опроса")
    created_by = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.CASCADE, 
        related_name='surveys_created', 
        verbose_name="Автор опроса"
    )
    company = models.ForeignKey(
        'users.Company',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='surveys_for_companys',
        verbose_name="Компания"
    )
    department = models.ForeignKey(
        'users.Department',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='surveys_for_department',
        verbose_name="Отдел"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    recipient_email = models.EmailField(verbose_name="Email получателя результатов")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Опрос"
        verbose_name_plural = "Опросы"


class SurveyQuestion(models.Model):
    """
    Модель вопроса опроса.
    Каждый вопрос связан с конкретным опросом и содержит текст вопроса.
    """
    survey = models.ForeignKey(
        'Survey', 
        on_delete=models.CASCADE, 
        related_name='questions', 
        verbose_name="Опрос"
    )
    text = models.TextField(verbose_name="Текст вопроса")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Вопрос опроса"
        verbose_name_plural = "Вопросы опроса"


class SurveyAnswerOption(models.Model):
    """
    Модель варианта ответа на вопрос опроса.
    Каждый вариант связан с конкретным вопросом и содержит текст варианта.
    """
    question = models.ForeignKey(
        'SurveyQuestion', 
        on_delete=models.CASCADE, 
        related_name='options', 
        verbose_name="Вопрос"
    )
    text = models.CharField(max_length=255, verbose_name="Текст варианта")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Вариант ответа опроса"
        verbose_name_plural = "Варианты ответов опроса"


class SurveyResponse(models.Model):
    """
    Модель результата прохождения опроса.
    Связывает опрос, сотрудника и дату прохождения.
    """
    survey = models.ForeignKey(
        'Survey', 
        on_delete=models.CASCADE, 
        related_name='responses', 
        verbose_name="Опрос"
    )
    user = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        related_name='survey_responses', 
        verbose_name="Сотрудник"
    )
    submitted_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата прохождения")

    def __str__(self):
        return f"Ответ {self.user} на опрос {self.survey}"

    class Meta:
        verbose_name = "Результат опроса"
        verbose_name_plural = "Результаты опросов"


class SurveyAnswer(models.Model):
    """
    Модель ответа на вопрос опроса.
    Связывает результат опроса, вопрос и выбранный вариант ответа.
    """
    response = models.ForeignKey(
        'SurveyResponse', 
        on_delete=models.CASCADE, 
        related_name='answers', 
        verbose_name="Результат опроса"
    )
    question = models.ForeignKey(
        'SurveyQuestion', 
        on_delete=models.CASCADE, 
        related_name='answers', 
        verbose_name="Вопрос"
    )
    selected_option = models.ForeignKey(
        'SurveyAnswerOption', 
        on_delete=models.CASCADE, 
        related_name='selected_in', 
        verbose_name="Выбранный вариант"
    )

    def __str__(self):
        return f"Ответ на вопрос {self.question}"

    class Meta:
        verbose_name = "Ответ на вопрос опроса"
        verbose_name_plural = "Ответы на вопросы опроса"