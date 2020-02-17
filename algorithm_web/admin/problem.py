from django.contrib import admin

from .. import models


@admin.register(models.Problem)
class ProblemeAdmin(admin.ModelAdmin):
    """
    문제관리
    """
    list_display = ['problem_name', 'limit_time', 'limit_memory', 'scoring_type', 'level', 'info', 'is_open', 'checker_code']

    class Meta:
        model = models.Problem


@admin.register(models.ProblemSet)
class ProblemSetAdmin(admin.ModelAdmin):
    """
    문제집관리
    """
    list_display = ['set_name', 'editor', 'message']

    class Meta:
        model = models.ProblemSet


@admin.register(models.ProblemList)
class ProblemListAdmin(admin.ModelAdmin):
    """
    문제집 문제관리
    """
    list_display = ['problem_set', 'problem']

    class Meta:
        model = models.ProblemList


@admin.register(models.TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    """
    테스트케이스관리
    """
    list_display = ['id', 'problem']

    class Meta:
        model = models.TestCase