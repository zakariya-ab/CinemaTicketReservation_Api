from django.db import models

# # Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length = 200, unique=True)
    description = models.TextField()
    duration = models.IntegerField()
    language = models.CharField(max_length=100)
    age_rating = models.CharField(max_length=10)
    release_date = models.DateField()
    poster_url = models.CharField(max_length=300)
    is_active = models.BooleanField()