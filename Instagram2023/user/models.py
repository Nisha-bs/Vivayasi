from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=12)
    created_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    is_staff = models.BooleanField(default=True, null=True, blank=True)
    is_admin = models.BooleanField(default=True, null=True, blank=True)

    def __str__(self):
        return self.username

class Farmer(models.Model):
    genders = (
        ("male", "Male"),
        ("female", "Female"),
        ("others", "Others")
    )

    farmer_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(choices=genders, max_length=9)
    father_or_husband_name = models.CharField(max_length=100)
    address = models.TextField()
    contact_number = models.CharField(max_length=12)
    whatsapp_number = models.CharField(max_length=12)
    local_or_outsider = models.CharField(max_length=9, null=True, blank=True)
    organic_farming = models.BooleanField(null=True, blank=True)
    single_seeding = models.BooleanField(null=True, blank=True)
    alternative_cropping = models.BooleanField(null=True, blank=True)
    seed_vareity_advice = models.BooleanField(null=True, blank=True)
    lease_own_land = models.BooleanField(null=True, blank=True)
    farm_rented_land = models.BooleanField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    is_staff = models.BooleanField(default=True, null=True, blank=True)
    is_admin = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.username

