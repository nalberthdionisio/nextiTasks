from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    date =  models.DateField()
    done = models.BooleanField(default=False)
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
