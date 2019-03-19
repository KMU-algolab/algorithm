from django.contrib import admin

from .. import models


@admin.register(models.Language)
class LanguageAdmin(admin.ModelAdmin):
    """
    언어관리
    """
    list_display = ['language', 'compile_message', 'run_message']

    class Meta:
        model = models.Language
