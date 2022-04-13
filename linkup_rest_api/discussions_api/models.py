from django.db import models
from django.contrib.auth.models import Group

# Create your models here.
class Discussion(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    admin = models.IntegerField()