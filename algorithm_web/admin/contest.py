from django.contrib import admin

from .. import models


@admin.register(models.Contest)
class ContestAdmin(admin.ModelAdmin):
    """
    대회관리
    """
    list_display = ['contest_name', 'start_time', 'end_time', 'message', 'after_open', 'order_type']

    class Meta:
        model = models.Contest


@admin.register(models.ContestProblem)
class ContestProblemAdmin(admin.ModelAdmin):
    """
    대회 문제관리
    """
    list_display = ['contest', 'problem']

    class Meta:
        model = models.ContestProblem


@admin.register(models.Participant)
class ParticipantAdmin(admin.ModelAdmin):
    """
    참가자관리
    """
    list_display = ['contest', 'participant']

    class Meta:
        model = models.Participant
