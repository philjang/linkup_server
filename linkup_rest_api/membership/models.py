from tkinter import CASCADE
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager # imports custom classes will inherit from
from rest_framework.authtoken.models import Token

# Create your models here.
# manager for user profiles -> provides functions for user model to use
class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('User must have a username')
        user = self.model(username=self.username, email=self.normalize_email(email))
        # built in django auth method to hash password
        user.set_password(password)
        # saves created user to db
        user.save()
        # always return user so it can be used when method is invoked
        return user
    
    def create_superuser(self, username, email, password=None):
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

# Model schema for custom user table abstracting default django auth user and permission mixins
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True) # no duplicate usernames
    email = models.EmailField(blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # ensures we use custom user manager above when we call User.objects (for objects.all() or objects.filter())
    objects = UserManager()

    # tells django to use the username field as the unique identifier
    USERNAME_FIELD = 'username' # not sure if needed, as username is default

    # this is what is prompted for when creating superuser
    # REQUIRED_FIELDS = ['name']

    def __str__(self):
        return f'user: {self.username} (id:{self.id})'

    def get_auth_token(self):
        Token.objects.filter(user=self).delete() # deletes current token if existing
        token = Token.objects.create(user=self) # creates new token
        self.token = token.key # assigns token to current user
        self.save()
        return token.key

    def delete_token(self):
        Token.objects.filter(user=self).delete()
        self.token = None
        self.save()
        return self


# Model schema for group table
class Group(models.Model):
    users = models.ManyToManyField(get_user_model(), related_name='groups', through='Membership', through_fields=('group','user'))
    name = models.CharField(max_length=255)
    admin = models.IntegerField()

    def __str__(self):
        return f'group: {self.name}, (id:{self.id})'

# custom join table - allows extra fields if needed
class Membership(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)