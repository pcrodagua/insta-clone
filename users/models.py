from django.db import models


# Create your models here.

class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    is_admin = models.BooleanField(default=False)
    bio = models.TextField(blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)

    # metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
