from django.db import models
from django.contrib.auth.models import User

from .problem import Problem
from .language import Language

STATUS_TYPE = (
    ('ING', '채점중'),
    ('SOL', '정답'),
    ('TER', '시간초과'),
    ('MER', '메모리초과'),
    ('CER', '컴파일에러'),
    ('RER', '런타임에러'),
    ('SER', '서버에러'),
)


class Submit(models.Model):
    """
    Submit
    """
    id = models.AutoField(
        '서로게이트키',
        db_column='SubmitId',
        primary_key=True,
        null=False,
    )

    user = models.ForeignKey(
        User,
        verbose_name='제출자(사용자)',
        db_column='User',
        primary_key=False,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )

    problem = models.ForeignKey(
        Problem,
        verbose_name='문제',
        db_column='Problem',
        primary_key=False,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )

    language = models.ForeignKey(
        Language,
        verbose_name='언어',
        db_column='Language',
        primary_key=False,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )

    status = models.CharField(
        '채점상태',
        db_column='Status',
        blank=False,
        null=False,
        max_length=3,
        choices=STATUS_TYPE,
    )

    def __str__(self):
        return '{}, {}, {}'.format(self.id, self.user.username, self.problem.problem_name)

    class Meta:
        db_table = 'SUBMIT'
        ordering = ['id', 'user__id']
        verbose_name = '제출: 제출정보'
        verbose_name_plural = '제출: 제출정보'
