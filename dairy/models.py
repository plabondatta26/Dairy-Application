from django.db import models

# Create your models here.

class Dairy(models.Model):
    title= models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=1000, blank=False)
    created_on = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
