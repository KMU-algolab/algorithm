import json as simplejson

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import User
from algorithm_web.models.problem import Problem
from algorithm_web.forms.problem import ProblemForm, TestCaseFormset, InputOnlyFormset


@method_decorator(csrf_exempt, name='dispatch')
class ManageManagerView(TemplateView):
    template_name = 'managemanager.html'

    def get(self, request, *arg, **kwargs):
        return render(request, self.template_name, {'managers': User.objects.filter(is_staff=True).all()})

    def post(self, request, *arg, **kwargs):
        if request.POST['req'] == 'add':
            sq = User.objects.filter(username__contains=request.POST['username']).first()

            if sq is None:
                response = JsonResponse({"error": "존재하지 않는 사용자 입니다."})
                response.status_code = 410
                return response

            elif sq.is_staff is True:
                response = JsonResponse({"error": "이미 관리자로 등록된 사용자입니다."})
                response.status_code = 403
                return response

            sq.is_staff = True
            sq.save()

            data = {'rendered_table': render_to_string('managerlist.html', context={'managers': User.objects.filter(is_staff=True).all()})}

            return JsonResponse(data)

        else:
            sq = User.objects.filter(username__contains=request.POST['username'].split()[0]).first()

            if sq is None:
                response = JsonResponse({"error": "존재하지 않는 사용자 입니다."})
                response.status_code = 410
                return response

            sq.is_staff = False
            sq.save()

            data = {'rendered_table': render_to_string('managerlist.html',
                                                       context={'managers': User.objects.filter(is_staff=True).all()})}

            return JsonResponse(data)
