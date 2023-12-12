
from django.db import models

class student(models.Model):
    name=models.CharField(max_length=50)
    roll=models.IntegerField()
    city=models.CharField(max_length=50)
    
class userOtp(models.Model):
    otp=models.CharField(max_length=200)
    username=models.CharField(max_length=500)