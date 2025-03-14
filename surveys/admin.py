from django.contrib import admin
from .models import Survey, SurveyQuestion, SurveyAnswerOption, SurveyResponse, SurveyAnswer


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_by', 'company', 'department', 'created_at', 'recipient_email')


@admin.register(SurveyQuestion)
class SurveyQuestionAdmin(admin.ModelAdmin):
    list_display = ('survey', 'text')


@admin.register(SurveyAnswerOption)
class SurveyAnswerOptionAdmin(admin.ModelAdmin):
    list_display = ('question', 'text')


@admin.register(SurveyResponse)
class SurveyResponseAdmin(admin.ModelAdmin):
    list_display = ('survey', 'user', 'submitted_at')


@admin.register(SurveyAnswer)
class SurveyAnswerAdmin(admin.ModelAdmin):
    list_display = ('response', 'question', 'selected_option')