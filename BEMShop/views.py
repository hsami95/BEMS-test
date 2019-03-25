from django.shortcuts import render
from .forms import MessageForm
from .models import Services


def index(request):

    services_list = Services.objects.all()
    context = {'services_list': services_list}
    return render(request, 'BEMShop/index.html', context)
