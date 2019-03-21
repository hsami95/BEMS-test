from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from models import Services


def index(request):
    template = loader.get_template('BEMShop/index.html')
    services_list = Services.objects[:6]
    context = {'services_list ': services_list}
    return HttpResponse(template.render(context, request))



