from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.signals import request_finished
from django.db.models.signals import post_save,pre_save

class EmailData(models.Model):
    email=models.EmailField(max_length=254)
    verify =models.EmailField(max_length=254)
    Designation = models.CharField(max_length=250)
    project = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    message = models.TextField()


    def __str__(self):
        return self.email
