from django.shortcuts import render
from .forms import MessageForm
from .models import Services


def index(request):
    services_list = Services.objects.all()[:6]
    context = {'services_list': services_list, 'form': MessageForm()}
    return render(request, 'BEMShop/index.html', context)
