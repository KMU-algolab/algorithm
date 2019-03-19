from django.db import models
from django.contrib.auth.models import User


LEVEL_TYPE = (
    (0, '하'),
    (1, '중'),
    (2, '상'),
)

def set_FK_Model_test():
    return User.objects.get(id=1)


class Problem(models.Model):
    """
    Problem
    """
    id = models.AutoField(
        '서로게이트키',
        db_column='ProblemId',
        primary_key=True,
        null=False,
    )

    problem_name = models.CharField(
        '문제 이름',
        db_column='ProblemName',
        max_length=60,
        blank=False,
        null=False,
    )

    limit_time = models.PositiveSmallIntegerField(
        '제한 시간',
        db_column='LimitTime',
        blank=False,
        null=False,
    )

    limit_memory = models.PositiveSmallIntegerField(
        '제한 메모리',
        db_column='LimitMemory',
        blank=False,
        null=False,
    )

    level = models.PositiveSmallIntegerField(
        '난이도',
        db_column='Level',
        blank=False,
        null=False,
        choices=LEVEL_TYPE,
    )

    is_open = models.BooleanField(
        '공개여부',
        db_column='isOpen',
        blank=False,
        null=False,
        default=True,
    )

    def __str__(self):
        return '{}, {}'.format(self.id, self.problem_name)

    class Meta:
        db_table = 'PROBLEM'
        ordering = ['id', 'problem_name']
        verbose_name = '문제: 문제'
        verbose_name_plural = '문제: 문제'


class TestCase(models.Model):
    """
    Problem Test Case
    """
    id = models.AutoField(
        '서로게이트키',
        db_column='TestCaseId',
        primary_key=True,
        null=False,
    )

    problem = models.ForeignKey(
        Problem,
        verbose_name='문제',
        db_column='ProblemId',
        blank=False,
        null=False,
        primary_key=False,
        on_delete=models.CASCADE,
    )

    input_data = models.TextField(
        '입력 데이터',
        db_column='InputData',
        blank=False,
        null=False,
    )

    output_data = models.TextField(
        '출력 데이터',
        db_column='OutputData',
        blank=False,
        null=False,
    )

    def __str__(self):
        return '{}, {}, {}'.format(self.id, self.problem.id, self.problem.problem_name)

    class Meta:
        db_table = 'TEST_CASE'
        ordering = ['id', 'problem__id']
        verbose_name = '문제: 테스트 케이스'
        verbose_name_plural = '문제: 테스트 케이스'


class ProblemSet(models.Model):
    """
    Problem Set
    """
    id = models.AutoField(
        '서로게이트키',
        db_column='ProblemSetId',
        primary_key=True,
        null=False,
    )

    editor = models.ForeignKey(
        User,
        verbose_name='편집자(사용자)',
        db_column='Editor',
        primary_key=False,
        blank=False,
        null=False,
        on_delete=models.SET(set_FK_Model_test),

    )

    set_name = models.CharField(
        '문제집 이름',
        db_column='SetName',
        max_length=50,
        blank=False,
        null=False,
    )

    message = models.CharField(
        '문제집 정보',
        db_column='Message',
        max_length=100,
        blank=False,
        null=False,
    )

    def __str__(self):
        return '{}, {}, {}'.format(self.id, self.editor.username, self.set_name)

    class Meta:
        db_table = 'PROBLEM_SET'
        ordering = ['id', 'editor__id']
        verbose_name = '문제: 문제집'
        verbose_name_plural = '문제: 문제집'


class ProblemList(models.Model):
    """
    Problem List in Problem Set
    """
    id = models.AutoField(
        '서로게이트키',
        db_column='ProblemListId',
        primary_key=True,
        null=False,
    )

    problem_set = models.ForeignKey(
        ProblemSet,
        verbose_name='문제집',
        db_column='ProblemSet',
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

    def __str__(self):
        return '{}, {}, {}'.format(self.id, self.problem_set.set_name, self.problem.problem_name)

    class Meta:
        db_table = 'PROBLEM_LIST'
        ordering = ['id', 'problem_set__id']
        unique_together = ('problem_set', 'problem',)
        verbose_name = '문제: 문제집 문제'
        verbose_name_plural = '문제: 문제집 문제'