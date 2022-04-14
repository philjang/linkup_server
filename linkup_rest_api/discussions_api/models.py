from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import Group, User

# Create your models here.
# Model schema for discussions_api_discussion table
class Discussion(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='discussions')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    admin = models.IntegerField()

    def __str__(self):
        return self.name

# Model schema for discussions_api_post table
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    time_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content