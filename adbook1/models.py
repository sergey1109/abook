from django.db import models

# Create your models here.

class Users(models.Model):

    name = models.CharField(max_length=255, unique=True, blank=False)
    surname = models.CharField(max_length=255, unique=True, blank=False)

    address_country = models.CharField(max_length=255, blank=True)
    address_sity = models.CharField(max_length=255, blank=True)
    address_street = models.CharField(max_length=255, blank=True)

    url = models.URLField(max_length=255, blank=True)

    phone_number = models.CharField(max_length=255, blank=True)
    img_user = models.ImageField(null=True, blank=True, upload_to="static/images/", max_length=255)

    def __str__(self):
        return self.name + self.surname


