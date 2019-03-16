from django.contrib import admin

from .. import models


@admin.register(models.UserInfo)
class StudentAdmin(admin.ModelAdmin):
    """
    학생관리
    """
    list_display = ['user', 'message']

    class Meta:
        model = models.UserInfo