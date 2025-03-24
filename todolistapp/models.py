from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class CustomUser(AbstractUser):
    phone_number=models.CharField(max_length=11, unique=True, blank=True, null=True)
    profile_picture=models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return self.username


class Taskers(models.Model):
    """ custom class list to our taskers"""
    username = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=500, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Task(models.Model):
    title = models.CharField(max_length=100, unique=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # est one-to-many relationships using FK
    taskers = models.ForeignKey(Taskers, on_delete=models.SET_NULL, null=True, blank=True)
    user=models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.title
""""
1. python manage.py migrate "appname" zero #resets migrations for the 
2. python manage.py makemigrations todolistapp
3. python manage.py migrate
"""