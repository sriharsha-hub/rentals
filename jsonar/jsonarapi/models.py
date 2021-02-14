from django.db import models
from django.contrib.auth.models import User

class Staff(models.Model):
    staffId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
# Create your models here.
class Customers(models.Model):
    # CustomerId=models.AutoField(primary_key=True,)
    Address = models.CharField(max_length=50)
    City = models.CharField(max_length=30)
    Country = models.CharField(max_length=30)
    District = models.CharField(max_length=30)
    Firstname=models.CharField(max_length=30)
    Lastname=models.CharField(max_length=30)
    Phone = models.BigIntegerField(null=True)
    def __str__(self):
        return self.Firstname

class Actors(models.Model):
    actorId = models.AutoField(primary_key=True)
    Firstname=models.CharField(max_length=30)
    Lastname=models.CharField(max_length=30)

    def __str__(self):
        return self.Firstname

class Films(models.Model):
    # FlimId=models.AutoField(primary_key=True,null=False)
    actors=models.ManyToManyField(Actors)
    Title=models.CharField(max_length=20)
    Category=models.CharField(max_length=30,null=True)
    Rating=models.CharField(max_length=10,null=True)
    Rental_duration=models.CharField(max_length=10,null=True)
    Length=models.CharField(max_length=10,null=True)
    Special_features=models.TextField(null=True)
    Description=models.TextField(null=True)
    actors = models.ManyToManyField(Actors)
    def __str__(self):
        return self.Title

class Rentals(models.Model):
    rentalId=models.AutoField(primary_key=True)
    CustomerId = models.ForeignKey(Customers,on_delete=models.CASCADE,null=True)
    FilmId = models.ForeignKey(Films,on_delete=models.CASCADE,null=True)
    StaffId = models.ForeignKey(Staff,on_delete=models.CASCADE,null=True)
    # Amount=models.OneToOneField(Payment.Amount,on_delete=models.CASCADE)
    Rental_Date = models.DateTimeField(null=True)
    Return_Date = models.DateTimeField(null=True)
    # def __str__(self):
    #     return self.rentalId


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    CustomerId=models.ForeignKey(Customers,on_delete=models.CASCADE,null=True)
    Amount=models.CharField(max_length=30,null=True)
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE,null=True)
    rental = models.ForeignKey(Rentals,on_delete=models.CASCADE,null=True)
    Payment_Date=models.DateTimeField(null=True)
    # def __str__(self):
    #     return self.Amount














