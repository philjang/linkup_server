from django.contrib import admin

# Register your models here.
from .models import Discussion, Post

admin.site.register(Discussion)
admin.site.register(Post)