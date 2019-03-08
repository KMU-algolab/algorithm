from django.views.generic import View
from django.shortcuts import render

class index(View):
    template_name = 'index.html'

    def get(self, request, *arg, **kwargs):
        return render(request, self.template_name)