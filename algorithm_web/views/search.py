import json as simplejson
from django.http import HttpResponse
from django.contrib.auth.models import User


def user_search(request):
    search_qs = User.objects.filter(username__contains=request.GET['search']).all()

    results = []
    for r in search_qs:
        results.append(r.username)

    resp = request.GET['callback'] + '(' + simplejson.dumps(results) + ');'

    return HttpResponse(resp, content_type='application/json')