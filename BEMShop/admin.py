from django.contrib import admin
from .models import Services, Email, Products, Message
#from .forms import MessageForm


admin.site.register(Services)
admin.site.register(Email)
admin.site.register(Products)
admin.site.register(Message)
# Register your models here.
