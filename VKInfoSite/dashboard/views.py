from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .dash_app import *


def dash(request, **kwargs):
    #domain = request.POST['domain'][0]
    domain = 'ivan_nikitinn'
    return HttpResponse(dispatcher(request, domain))


@csrf_exempt
def dash_ajax(request):
    #domain = request.POST['domain'][0]
    domain = 'ivan_nikitinn'
    return HttpResponse(dispatcher(request, domain), content_type='application/json')