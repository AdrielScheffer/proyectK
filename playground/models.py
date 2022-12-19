from django.db import models
from django.urls import reverse
# Create your models here.

class Autists(models.Model):
    name = models.CharField(max_length=255,default='unamed')
    badOpinion = models.TextField(max_length=255)
    goodOpinion = models.TextField(max_length=255)

    
    def __str__(self):

        return self.name


    def get_absolute_url(self):
        return reverse('finalResult')

class Names(models.Model):
    name = models.CharField(max_length=255,default='unamed')

    def __str__(self):

        return self.name 

    