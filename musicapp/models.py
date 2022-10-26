from email.policy import default
from django.db import models
from datetime import datetime
# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()

class Song(models.Model):
    artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    date_released = models.DateField(default=datetime)
    likes = models.IntegerField()
    
    
class Lyric(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)