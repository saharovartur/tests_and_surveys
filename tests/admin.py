from django.contrib import admin
from .models import Test, TestQuestion, TestAnswerOption, TestResponse, TestAnswer


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_by', 'company', 'department', 'created_at', 'recipient_email')

@admin.register(TestQuestion)
class TestQuestionAdmin(admin.ModelAdmin):
    list_display = ('test', 'text')


@admin.register(TestAnswerOption)
class TestAnswerOptionAdmin(admin.ModelAdmin):
    list_display = ('question', 'text', 'is_correct')


@admin.register(TestResponse)
class TestResponseAdmin(admin.ModelAdmin):
    list_display = ('test', 'user', 'submitted_at')