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
        "상태 메시지",
        db_column="Message",
        max_length=60,
        blank=True,
        null=True,
    )

    def __str__(self):
        return '{}, {}'.format(self.user.username, self.message)

    class Meta:
        db_table = 'USER_INFORMATION'
        ordering = ['user__username', 'message']
        verbose_name = '사용자: 추가정보'
        verbose_name_plural = '사용자: 추가정보'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserInfo.objects.create(user=instance)