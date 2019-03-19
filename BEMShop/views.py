from django.http import HttpResponse
from django.shortcuts import render
from .forms import MessageForm
# Create your views here.
from django.template import loader

from .models import Services


def index(request):
    #template = loader.get_template('BEMShop/index.html')
    services_list = Services.objects.all()[:6]
    # for service in services_list:
    #     print(service)
    context = {'services_list': services_list, 'form': MessageForm()}
    return render(request, 'BEMShop/index.html', context)


# def post_new(request):
#     form = PostForm()
#     return render(request, 'blog/post_edit.html', {'form': form})
