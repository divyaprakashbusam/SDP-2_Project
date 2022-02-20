from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    gender = models.CharField(max_length=6)
    password = models.CharField(max_length=20)

class Admin(models.Model):
    aid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=20)

class Event(models.Model):
    eid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    duration = models.IntegerField()



class Book_ground(models.Model):
    bid = models.AutoField(primary_key=True)
    uid = models.IntegerField()
    name = models.CharField(max_length=20)
    email=models.EmailField()
    mobile = models.CharField(max_length=10)
    date = models.DateField()
    time = models.TimeField()
    venue=models.CharField(max_length=50)
    people = models.CharField(max_length=10)
    cat= models.CharField(max_length=6)
    event=models.CharField(max_length=80)
    deco=models.CharField(max_length=40)
    price=models.FloatField()


class Events_list(models.Model):
    eventid = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100, null=True)
    price=models.FloatField()
    image=models.ImageField(null=True, blank=True)


class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.TextField()

    def __str__(self):
        return self.name
