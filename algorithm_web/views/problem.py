from django.shortcuts import render
from django.views.generic import TemplateView

from algorithm_web.models.problem import Problem
from algorithm_web.forms.submit import SubmitForm


class Problems(TemplateView):
    template_name = 'problemlist.html'

    def get(self, request, *arg, **kwargs):
        return render(request, self.template_name, {'problems': Problem.objects.filter().all(),
                                                    'exp': round(self.request.user.extrainformation.possession_exp /
                                                                 self.request.user.extrainformation.next_exp * 100, 1)})


class Submit(TemplateView):
    template_name = 'submit.html'

    def get(self, request, *arg, **kwargs):
        problem = Problem.objects.values('id', 'problem_name', 'problem_text', 'limit_time', 'limit_memory', 'level',
                                     'scoring_type', 'info').get(id=kwargs['id'])

        return render(request, self.template_name, {'problem': problem, 'form': SubmitForm()})
