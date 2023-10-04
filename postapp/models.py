from django.db import models

# Create your models here.
class Sample(models.Model):
  fname = models.CharField(max_length=50)
  lname = models.CharField(max_length=50)
  address = models.CharField(max_length=100)
  place = models.CharField(max_length=100)
