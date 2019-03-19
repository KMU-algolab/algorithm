import datetime

from django.shortcuts import render
from django.views.generic import TemplateView

from ..models.user import ExtraInformation


class MyPage(TemplateView):
    template_name = 'mypage.html'

    def get(self, request, *arg, **kwargs):
        return render(request, self.template_name, {'user': self.request.user,
                                                    'exp': round(self.request.user.extrainformation.possession_exp /
                                                                 self.request.user.extrainformation.next_exp * 100, 1)})

    def post(self, request, *arg, **kwargs):
        qs = ExtraInformation.objects.get(user_id=self.request.user.id)
        qs.message = self.request.POST['message']
        qs.save()
        return render(request, self.template_name, {'user': self.request.user,
                                                    'exp': round(self.request.user.extrainformation.possession_exp /
                                                                 self.request.user.extrainformation.next_exp * 100, 1)})
