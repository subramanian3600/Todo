from django.db import models
from django.forms import ModelForm

class Task(models.Model):
    title=models.CharField(max_length=20,unique=True)
    check=models.BooleanField(default=False)
    
    def __str__(self):
        return self.title