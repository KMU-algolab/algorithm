from django.shortcuts import render
from django.views.generic import TemplateView

from algorithm_web.models.problem import Problem


class Problems(TemplateView):
    template_name = 'problemlist.html'

    def get(self, request, *arg, **kwargs):
        return render(request, self.template_name, {'problems': Problem.objects.filter().all(),
                                                    'exp': round(self.request.user.extrainformation.possession_exp /
                                                                 self.request.user.extrainformation.next_exp * 100, 1)})

    def post(self, request, *arg, **kwargs):
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!')
        # qs = ExtraInformation.objects.get(user_id=self.request.user.id)
        # qs.message = self.request.POST['message']
        # qs.save()
        return render(request, 'problem.html', {'user': self.request.user,
                                                    'exp': round(self.request.user.extrainformation.possession_exp /
                                                                 self.request.user.extrainformation.next_exp * 100, 1)})
