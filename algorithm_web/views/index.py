import datetime

from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *arg, **kwargs):
        if not self.request.user.is_anonymous:
            if (datetime.datetime.now() - self.request.user.date_joined).seconds < 5:
                # redirect user page
                pass
        return render(request, self.template_name)
