from django.db import models

# Create your models here.
class Cheese(models.Model):
    name = models.CharField(max_length=100)
    origin_country = models.CharField(max_length=100)
    typeOfCheese = models.CharField(max_length=100)