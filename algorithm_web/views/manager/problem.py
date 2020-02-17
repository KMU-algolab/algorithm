from django.shortcuts import render
from django.views.generic import TemplateView

from algorithm_web.models.problem import Problem
from algorithm_web.forms.problem import ProblemForm, TestCaseFormset, InputOnlyFormset


class ManageProblems(TemplateView):
    template_name = 'manageproblem.html'

    def get(self, request, *arg, **kwargs):
        return render(request, self.template_name, {'problems': Problem.objects.filter().all()})


class CreateProblems(TemplateView):
    def get(self, request, *arg, **kwargs):
        problem = ProblemForm(initial={'level': 1, 'limit_time': 1000, 'limit_memory': 128, 'scoring_type': True})
        testcase = TestCaseFormset(prefix='testcase')
        input_only = InputOnlyFormset(prefix='inputOnly')
        return render(request, 'create_problem.html', {'problem': problem, 'testcase': testcase,
                                                       'input_only': input_only})

    def post(self, request, *arg, **kwargs):
        problem = ProblemForm(request.POST)
        testcases = TestCaseFormset(request.POST, prefix='testcase')
        inputcases = InputOnlyFormset(request.POST, prefix='inputOnly')

        if problem.is_valid() and (testcases.is_valid() or inputcases.is_valid()):
            post_problem = problem.save(commit=False)
            is_solution = post_problem.scoring_type
            post_problem.save()

            if is_solution:
                for testcase in testcases:
                    if testcase.is_valid():
                        post_testcase = testcase.save(commit=False)
                        if len(post_testcase.input) > 0:
                            post_testcase.problem = post_problem
                            post_testcase.save()
            else:
                for input in inputcases:
                    if input.is_valid():
                        post_input = input.save(commit=False)
                        if len(post_input.input) > 0:
                            post_input.problem = post_problem
                            post_input.save()


        return render(request, 'problemlist.html', {'problems': Problem.objects.filter().all()})