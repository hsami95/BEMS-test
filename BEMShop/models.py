from django.db import models


class Services(models.Model):
    title = models.CharField(max_length=300, default="")
    description = models.TextField(default="")


class Email(models.Model):
    email = models.EmailField()


class Products(models.Model):
    category_choices = (
        ('Android', 'Android'),
        ('Iphone', 'Iphone'),
        ('Accessories', 'Accessories'),
    )
    product_image = models.ImageField(upload_to='uploaded_media',
                                      default='uploaded_media/None/No-image.jpg', null=True, blank=True)
    title = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=category_choices)


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=500)
