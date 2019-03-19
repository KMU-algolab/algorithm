from django.contrib import admin

from .. import models


@admin.register(models.ExtraInformation)
class ExtraInformationAdmin(admin.ModelAdmin):
    """
    추가정보관리
    """
    list_display = ['user', 'message', 'level', 'possession_exp']

    class Meta:
        model = models.ExtraInformation