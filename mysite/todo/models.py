from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

class Task(models.Model):
    title=models.CharField(max_length=20,unique=True)
    check=models.BooleanField(default=False)
    
    def __str__(self):
        return self.title