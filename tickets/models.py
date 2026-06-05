from django.db import models

# Create your models here.

class Movie(models.Model):
    hall = models.CharField(max_length=20)
    movie = models.CharField(max_length=200)
    date = models.DateField()

class Guest(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)

class Reservation(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reservation')
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name='reservation')