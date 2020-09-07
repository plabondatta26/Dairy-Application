from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Dairy(models.Model):
    title= models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now=True)
    user= models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
