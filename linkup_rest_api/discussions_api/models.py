from tkinter import CASCADE
from django.db import models
from django.contrib.auth import get_user_model
from ..membership.models import Group

# Create your models here.
# Model schema for discussions_api_discussion table
class Discussion(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='discussions') # related_name allows access to an array of this model's instances from the related 1:M model's serializer/view
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    admin = models.IntegerField()

    def __str__(self):
        return f'The discussion topic: {self.name} - {self.description} (id:{self.id})'

# Model schema for discussions_api_post table
class Post(models.Model):
    # considered best practice to get user model using 'get_user_model'
    # this method will ensure the User model comes from settings.py file (AUTH_USER_MODEL = 'membership.User')
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='posts')
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    time_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'post: {self.content}, by: {self.owner} (id:{self.id})'