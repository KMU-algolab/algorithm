from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserInfo(models.Model):
    """
    User Extra Information
    """
    user = models.OneToOneField(
        User,
        verbose_name='사용자',
        db_column='User',
        primary_key=True,
        on_delete=models.CASCADE,
    )

    message = models.CharField(
        '상태 메시지',
        db_column='Message',
        max_length=60,
        blank=True,
        null=True,
    )

    level = models.PositiveSmallIntegerField(
        '레벨',
        db_column='Level',
        blank=False,
        null=False,
        default=1,
    )

    next_exp = models.PositiveIntegerField(
        '다음 경험치',
        db_column='NextEXP',
        blank=False,
        null=False,
        default=100,
    )

    possession_exp = models.PositiveIntegerField(
        '보유 경험치',
        db_column='PossessionEXP',
        blank=False,
        null=False,
        default=0,
    )

    def __str__(self):
        return '{}, {}'.format(self.user.username, self.message)

    class Meta:
        db_table = 'USER_INFORMATION'
        ordering = ['user__username', 'message', 'level']
        verbose_name = '사용자: 추가정보'
        verbose_name_plural = '사용자: 추가정보'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserInfo.objects.create(user=instance)