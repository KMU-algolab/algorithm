from itertools import chain

from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import TemplateView
from django.db.models.functions import Coalesce
from django.db.models import Count, F, Q, FloatField, ExpressionWrapper

from algorithm_web.forms.submit import SubmitForm
from algorithm_web.models.problem import Problem, ProblemSet


class ProblemsView(TemplateView):
    template_name = 'problemlist.html'

    def get(self, request, *arg, **kwargs):
        if 'id' in kwargs:
            problem = Problem.objects.values('id', 'problem_name', 'problem_text', 'limit_time', 'limit_memory',
                                             'level', 'scoring_type', 'info').get(id=kwargs['id'])

            return render(request, self.template_name, {'problem': problem, 'form': SubmitForm()})

        return render(request, self.template_name, {'problems': Problem.objects.filter().all()})


class ProblemSetView(TemplateView):
    template_name = 'problemsetlist.html'

    def get(self, request, *arg, **kwargs):
        problemsets = ProblemSet.objects.values('id').\
            annotate(problem_cnt=Count('problemlist__problem', output_field=FloatField()),
                     solve_cnt=Count('problemlist__problem__submit__status',
                                     filter=Q(problemlist__problem__submit__user=self.request.user,
                                              problemlist__problem__submit__status='SOL'), output_field=FloatField())).\
            annotate(rate=Coalesce(ExpressionWrapper(F('solve_cnt') * 100.0 / F('problem_cnt'), output_field=FloatField()), 0.0)).\
            values('id', 'editor__username', 'set_name', 'problem_cnt', 'solve_cnt', 'rate')

        return render(request, self.template_name, {'problemsets': problemsets})

    def post(self, request, *arg, **kwargs):
        ProblemSet.objects.create(editor=self.request.user,
                                  set_name=self.request.POST['set_name'],
                                  message=self.request.POST['message'])

        problemsets = ProblemSet.objects.values('id'). \
            annotate(problem_cnt=Count('problemlist__problem', output_field=FloatField()),
                     solve_cnt=Count('problemlist__problem__submit__status',
                                     filter=Q(problemlist__problem__submit__user=self.request.user,
                                              problemlist__problem__submit__status='SOL'), output_field=FloatField())). \
            annotate(rate=Coalesce(ExpressionWrapper(F('solve_cnt') * 100.0 / F('problem_cnt'), output_field=FloatField()), 0.0)). \
            values('id', 'editor__username', 'set_name', 'problem_cnt', 'solve_cnt', 'rate')

        return render(request, self.template_name, {'problemsets': problemsets})


class ProblemsInSetView(TemplateView):
    template_name = 'problemlistinset.html'

    def get(self, request, *arg, **kwargs):
        return render(request, self.template_name,
                      {'problems': Problem.objects.filter(problemlist__problem_set__id=kwargs['id']).all()})



class SubmitView(TemplateView):
    template_name = 'submit.html'

    def get(self, request, *arg, **kwargs):
        problem = Problem.objects.values('id', 'problem_name', 'problem_text', 'limit_time', 'limit_memory', 'level',
                                         'scoring_type', 'info').get(id=kwargs['id'])

        return render(request, self.template_name, {'problem': problem, 'form': SubmitForm()})