from django.db import models
#from django.contrib.sites.models import Site


class Services(models.Model):
    service_title = models.CharField(max_length=300)
    service_description = models.TextField()


class Email(models.Model):
    email = models.EmailField()
    #site = models.OneToOneField(Site)


class Products(models.Model):
    product_image = models.ImageField(upload_to='uploaded_media',
                                      default='uploaded_media/None/No-image.jpg', null=True, blank=True)
    product_title = models.CharField(max_length=100)
    product_price = models.CharField(max_length=10)


class Message(models.Model):
    name = models.CharField(max_length=100, default='Please enter your name here...')
    email = models.EmailField()
    subject = models.CharField(max_length=200, default='Please enter your subject here...')
    message = models.TextField(max_length=500, default='Please enter your message here...')






