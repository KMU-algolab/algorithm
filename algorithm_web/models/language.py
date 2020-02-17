from django.db import models


class Language(models.Model):
    """
    Language
    """
    id = models.AutoField(
        '서로게이트키',
        db_column='LanguageId',
        primary_key=True,
        null=False,
    )

    language = models.CharField(
        '언어',
        db_column='Language',
        max_length=50,
        blank=False,
        null=False,
    )

    compile_message = models.CharField(
        '컴파일 메시지',
        db_column='CompileMessage',
        max_length=100,
        blank=False,
        null=False,
    )

    run_message = models.CharField(
        '실행 메시지',
        db_column='RunMessage',
        max_length=100,
        blank=False,
        null=False,
    )

    def __str__(self):
        return '{}'.format(self.language)

    class Meta:
        db_table = 'LANGUAGE'
        ordering = ['id', 'language']
        verbose_name = '언어: 언어'
        verbose_name_plural = '언어: 언어'
