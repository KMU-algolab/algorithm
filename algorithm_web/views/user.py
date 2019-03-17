import datetime

from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from ..models.userinfo import UserInfo


class MyPage(TemplateView):
    template_name = 'mypage.html'

    def get(self, request, *arg, **kwargs):
        return render(request, self.template_name, {'user': self.request.user,
                                                    'exp': int(self.request.user.userinfo.possession_exp /
                                                               self.request.user.userinfo.next_exp * 100)})
