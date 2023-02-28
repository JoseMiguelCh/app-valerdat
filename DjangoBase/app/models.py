from django.db import models

class Product(models.Model):
    reference = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    volume = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)