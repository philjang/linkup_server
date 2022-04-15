from django.db import models


# Create your models here.
# Model schema for custom user table abstracting default django auth user
class User(models.Model):
    pass

# Model schema for group table
class Group(models.Model):
    # considered best practice to get user model using 'get_user_model'
    # this method will nesure the User model comes from settings.py file (AUTH_USER_MODEL = 'membership.User')
    pass