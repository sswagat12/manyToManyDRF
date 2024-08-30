from django.db import models

# Create your models here.
from django.db import models



class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20)
    addresses = models.ManyToManyField('UserAddress', related_name='users')

    def __str__(self) -> str:
        return f"{self.name} ({self.email})"

class UserAddress(models.Model):
    home = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.address}, {self.city}, {self.state} - {self.pincode}"