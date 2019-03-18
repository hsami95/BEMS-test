from django.db import models
#from django.contrib.sites.models import Site


class Services(models.Model):
    service_title = models.CharField(max_length=300)
    service_description = models.TextField()


#class Email(models.Model):
#    site = models.OneToOneField(Site)
#    email = models.EmailField()

