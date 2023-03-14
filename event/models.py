from django.db import models

# Create your models here.

class events(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    desc=models.CharField(max_length=1000)
    date=models.DateField()



