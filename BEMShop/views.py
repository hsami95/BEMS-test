from django.shortcuts import render
from .forms import MessageForm
from .models import Services, Products


def index(request):
    form = MessageForm(request.POST or None)
    if form.is_valid():
        form.save()
    services_list = Services.objects.all()
    products = Products.objects.all()
    context = {
        'services_list': services_list,
        'products': products,
        'form': form}
    return render(request, 'BEMShop/index.html', context)
