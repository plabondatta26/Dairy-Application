from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Dairy(models.Model):
    title = models.CharField(max_length=100, blank=False, unique=False)
    description = models.TextField(blank=False, unique=False)
    created_on = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, blank=False,unique=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.title