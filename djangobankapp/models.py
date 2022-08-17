
# Create your models here.
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Gender(models.Model):
    gender=models.CharField(max_length=50)

    def __str__(self):
        return self.gender


class Account(models.Model):
    acc_type=models.CharField(max_length=200)

    def __str__(self):
        return self.acc_type



class Person(models.Model):
    name = models.CharField(max_length=124)
    dob=models.DateField(auto_now_add=True)
    age=models.CharField(max_length=10)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    Email = models.EmailField()
    Mobile = models.CharField(max_length=15)
    Address = models.TextField()

    district = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
    Account_type = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.name