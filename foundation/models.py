from django.db import models

# Create your models here.
class Foundation(models.Model):
    Foundation_Name = models.CharField(max_length=100)
    Focus_area      = models.TextField(blank=True,null=True) 
    Address         = models.CharField(max_length=100)
    Email           = models.EmailField(max_length=100)
    Phone           = models.CharField(max_length=20)
    Website         = models.URLField(blank=True,null=True)

