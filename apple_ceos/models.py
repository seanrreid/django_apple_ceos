from django.db import models

# Create your models here.

class CEO(models.Model):
    """Model representing a CEO."""
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    year = models.IntegerField(null=False)
