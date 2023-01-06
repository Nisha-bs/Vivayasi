from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=12)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=True, blank=True)
    is_admin = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return self.username

class Farmer(models.Model):
    pass