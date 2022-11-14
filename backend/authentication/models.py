from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
    '''
    This is a custom version of the built in User class
    It contains all of the built in fields and functionality of the standard User
    You can add fields here for any additional properties you want a User to have
    This is useful for adding roles (Customer and Employee, for example)
    For just a few roles, adding boolean fields is advised
    '''
    # Example (note import of models above that is commented out)
    # this will add a column to the user table
    # is_student = models.BooleanField('student status', default=False)
    address= models.CharField(max_length=255)
    city= models.CharField(max_length=255)
    state= models.CharField(max_length=255)
    zip_code= models.IntegerField()
    phone_number= models.IntegerField()


class Pet(models.Model):
    name= models.CharField(max_length=255)
    age= models.IntegerField()
    temperament= models.CharField(max_length=255)

class Services(models.Model):
    user_id= models.ForeignKey(User, on_delete=models.CASCADE)
    pet_id= models.ForeignKey(Pet, on_delete=models.CASCADE)
    pet_name= models.ForeignKey(Pet, on_delete=models.CASCADE)
    start_date= models.DateField(null=True, blank=True)
    end_date= models.DateField(null=True, blank=True)

