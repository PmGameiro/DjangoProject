from django.db import models
from utils.model import Model
from django_extensions.db.models import ActivatorModel, TimeStampedModel


class Contact(ActivatorModel, TimeStampedModel, Model):
    class Meta:
        verbose_name_plural = "Contacts via website"

    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20)
    message = models.TextField(max_length=1000)
