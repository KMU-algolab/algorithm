from django.contrib import admin

from .. import models


@admin.register(models.Submit)
class SubmitAdmin(admin.ModelAdmin):
    """
     제출정보관리
    """
    list_display = ['id', 'user', 'problem', 'language', 'status']

    class Meta:
        model = models.Submit
