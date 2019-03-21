from django.db import models


class Services(models.Model):
    title = models.CharField(max_length=300, default="")
    description = models.TextField(default="")


class Email(models.Model):
    email = models.EmailField()


class Products(models.Model):
    product_image = models.ImageField(upload_to='uploaded_media',
                                      default='uploaded_media/None/No-image.jpg', null=True, blank=True)
    title = models.CharField(max_length=100)
    price = models.CharField(max_length=10)


class Message(models.Model):
    name = models.CharField(max_length=100, default='Please enter your name here...')
    email = models.EmailField()
    subject = models.CharField(max_length=200, default='Please enter your subject here...')
    message = models.TextField(max_length=500, default='Please enter your message here...')
