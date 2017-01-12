from django.db import models
import json
from django.http import JsonResponse

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    message = models.CharField(max_length = 100)

    def __str__(self):
        return '%s %s'%(self.first_name, self.last_name)
