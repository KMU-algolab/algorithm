from django.db import models
from django.contrib.auth.models import User
from algorithm_web.models.problem import Problem


ORDER_TYPE = (
    ('SP', '해결문제'),
    ('TS', '총점'),
)


class Contest(models.Model):
    """
    Contest
    """
    id = models.AutoField(
        '서로게이트키',
        db_column='ProblemId',
        primary_key=True,
        null=False,
    )

    contest_name = models.CharField(
        '대회명',
        db_column='ContestName',
        max_length=40,
        blank=False,
        null=False,
    )

    start_time = models.DateTimeField(
        '시작 시간',
        db_column='StartTime',
        blank=False,
        null=False,
    )

    end_time = models.DateTimeField(
        '종료 시간',
        db_column='EndTime',
        blank=False,
        null=False,
    )

    message = models.CharField(
        '대회소개',
        db_column='Message',
        max_length=100,
        blank=False,
        null=False,
    )

    host_email = models.EmailField(
        '개최자 메일',
        db_column='Host_Email',
        max_length=50,
        null=False,
        blank=False,
    )

    after_open = models.BooleanField(
        '문제공개여부',
        db_column='AfterOpen',
        blank=False,
        null=False,
        default=True,
    )

    def __str__(self):
        return '{}, {}'.format(self.id, self.contest_name)

    class Meta:
        db_table = 'CONTEST'
        ordering = ['id', 'contest_name']
        verbose_name = '대회: 대회'
        verbose_name_plural = '대회: 대회'


class ContestProblem(models.Model):
    """
    Problem using in Contest
    """
    id = models.AutoField(
        '서로게이트키',
        db_column='ContestProblemId',
        primary_key=True,
        null=False,
    )

    contest = models.ForeignKey(
        Contest,
        verbose_name='대회',
        db_column='Contest',
        primary_key=False,
        on_delete=models.CASCADE,
    )

    problem = models.ForeignKey(
        Problem,
        verbose_name='대회문제',
        db_column='Problem',
        primary_key=False,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return '{}, {}, {}'.format(self.id, self.contest.contest_name, self.problem.problem_name)

    class Meta:
        db_table = 'CONTEST_PROBLEM'
        ordering = ['id', 'contest__id', 'problem__id']
        unique_together = ('contest', 'problem',)
        verbose_name = '대회: 대회문제'
        verbose_name_plural = '대회: 대회문제'


class Participant(models.Model):
    """
    Participant in Contest
    """
    id = models.AutoField(
        '서로게이트키',
        db_column='ProblemId',
        primary_key=True,
        null=False,
    )

    contest = models.ForeignKey(
        Contest,
        verbose_name='대회',
        db_column='Contest',
        primary_key=False,
        on_delete=models.CASCADE,
    )

    participant = models.ForeignKey(
        User,
        verbose_name='참가사(사용자)',
        db_column='Participant',
        primary_key=False,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return '{}, {}, {}'.format(self.id, self.contest.contest_name, self.participant.username)

    class Meta:
        db_table = 'PARTICIPANT'
        ordering = ['id', 'contest__id', 'participant__id']
        unique_together = ('contest', 'participant',)
        verbose_name = '대회: 참가자'
        verbose_name_plural = '대회: 참가자'
