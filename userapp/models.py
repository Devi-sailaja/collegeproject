from django.db import models

# Create your models here.
class Farmstore(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    cost = models.IntegerField()
    mdate = models.DateField()

class Vegetables(models.Model):
    name = models.CharField(max_length=90)
    cost = models.IntegerField()

    def __str__(self):
        return self.name
class Customer(models.Model):
    cust_id=models.AutoField(primary_key=True)
    cust_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.cust_name