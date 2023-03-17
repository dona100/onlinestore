from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Mobiles(models.Model):
    name=models.CharField(max_length=200,unique=True)
    brand=models.CharField(max_length=200)
    price=models.PositiveBigIntegerField()
    specs=models.CharField(max_length=200)
    band=models.CharField(max_length=200)

    def __str__(self):
        return self.name
