from django.db import models

# Create your models here.

# Our Pet model's class with all of the data fields that it requires
class Pet(models.Model):

    name = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    age = models.CharField(max_length=50)
    type = models.CharField(max_length=30)
    gender = models.CharField(max_length=20)

    # Returns name when called as a string function.
    def __str__(self):
        return self.name
