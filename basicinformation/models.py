from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# Create your models here
class Information(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    location = models.CharField(max_length=140)
    def __str__(self):
        return self.first_name